import boto3
import io
import sys
import base64
from logging import Logger

rek_client = boto3.client('rekognition')
logger = Logger(name='FaceLivenessLambdaFunction')

class FaceLivenessError(Exception):
    '''
    Represents an error due to Face Liveness Issue.
    '''
    pass


def get_session_results(session_id):
    '''
    Get Session result.
    '''
    try:
        response = rek_client.get_face_liveness_session_results(SessionId=session_id)
        imageStream = io.BytesIO(response['ReferenceImage']['Bytes'])
        referenceImage = base64.b64encode(imageStream.getvalue())
        response['ReferenceImage']['Bytes'] = referenceImage

        return response
    except rek_client.exceptions.AccessDeniedException:
        logger.error('Access Denied Error')
        raise FaceLivenessError('AccessDeniedError')
    except rek_client.exceptions.InternalServerError:
        logger.error('InternalServerError')
        raise FaceLivenessError('InternalServerError')
    except rek_client.exceptions.InvalidParameterException:
        logger.error('InvalidParameterException')
        raise FaceLivenessError('InvalidParameterException')
    except rek_client.exceptions.SessionNotFoundException:
        logger.error('SessionNotFound')
        raise FaceLivenessError('SessionNotFound')
    except rek_client.exceptions.ThrottlingException:
        logger.error('ThrottlingException')
        raise FaceLivenessError('ThrottlingException')
    except rek_client.exceptions.ProvisionedThroughputExceededException:
        logger.error('ProvisionedThroughputExceededException')
        raise FaceLivenessError('ProvisionedThroughputExceededException')
   

def lambda_handler(event, context):
    output = get_session_results(event['sessionid'])
    return {
        'statusCode': 200,
        'body': (output)
    }


if __name__ == "__main__":
    session_id = sys.argv[1]
    status = get_session_results(session_id)

