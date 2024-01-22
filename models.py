CLARIFAI_PAT="4dadb44b7b694d349a3250a67bad1523"
######################################################################################################
# In this section, we set the user authentication, user and app ID, model details, and the URL of
# the text we want as an input. Change these strings to run your own example.
######################################################################################################

# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = '4478ab0e2f11437fb17aa1145fb51b1f'
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'clarifai'
APP_ID = 'main'
# Change these to whatever model and text URL you want to use
MODEL_ID = 'social-media-sentiment-english'
MODEL_VERSION_ID = 'fa9e29cb33f841b2832508cb41b30b44'
RAW_TEXT = '' ###---------------------------------------------------
# To use a hosted text file, assign the url variable
# TEXT_FILE_URL = 'https://samples.clarifai.com/negative_sentence_12.txt'
# Or, to use a local text file, assign the url variable
# TEXT_FILE_LOCATION = 'YOUR_TEXT_FILE_LOCATION_HERE'

############################################################################
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
############################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

def sentimentAnalyser(RAW_TEXT):
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    # To use a local text file, uncomment the following lines
    # with open(TEXT_FILE_LOCATION, "rb") as f:
    #    file_bytes = f.read()

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=RAW_TEXT
                            # url=TEXT_FILE_URL
                            # raw=file_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    # print("Predicted concepts:")
    # for concept in output.data.concepts:
    #     print("%s %.2f" % (concept.name, concept.value))
    z = {}

    for i in output.data.concepts:
        z[i.name] = i.value

    if z['positive'] > z['negative'] and z['positive'] > z['neutral']:
        score = round(z['positive']*10)
        # print(f"Positive,  Score = {score}")
            
        return 'Positive', score

    elif z['negative'] > z['positive'] and z['negative'] > z['neutral']:
        score =  round((1 - z['negative'])*10)
        # print('Negative', score)
        return 'Negative', score

    elif z['neutral'] > z['positive'] and z['neutral'] > z['negative']:
        score =  round((1 - z['negative'])*10)
        # print('Neutral', score)
        return 'Neutral', score

    # Uncomment this line to print the full Response JSON
    #print(output)

def convertor(RAW_TEXT):
        
    ######################################################################################################
    # In this section, we set the user authentication, user and app ID, model details, and the URL of 
    # the text we want as an input. Change these strings to run your own example.
    ######################################################################################################

    # Your PAT (Personal Access Token) can be found in the portal under Authentification
    PAT = 'bbb352e53fb048f5a5e9560d7ffb9343'
    # Specify the correct user_id/app_id pairings
    # Since you're making inferences outside your app's scope
    USER_ID = 'openai'
    APP_ID = 'chat-completion'
    # Change these to whatever model and text URL you want to use
    MODEL_ID = 'GPT-4'
    MODEL_VERSION_ID = '5d7a50b44aec4a01a9c492c5a5fcf387'
    # RAW_TEXT = 'I love your product very much'
    # To use a hosted text file, assign the url variable
    # TEXT_FILE_URL = 'https://samples.clarifai.com/negative_sentence_12.txt'
    # Or, to use a local text file, assign the url variable
    # TEXT_FILE_LOCATION = 'YOUR_TEXT_FILE_LOCATION_HERE'

    ############################################################################
    # YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
    ############################################################################

    from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
    from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
    from clarifai_grpc.grpc.api.status import status_code_pb2

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    # To use a local text file, uncomment the following lines
    # with open(TEXT_FILE_LOCATION, "rb") as f:
    #    file_bytes = f.read()

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=f"Convert the following text to have a positive sentiment: '{RAW_TEXT}'"
                            # url=TEXT_FILE_URL
                            # raw=file_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    convertedText = output.data.text.raw
    # print("Completion:\n")
    # print(convertedText[1:len(convertedText)-1])
    # return output.data.text.raw
    return convertedText[1:len(convertedText)-1]
