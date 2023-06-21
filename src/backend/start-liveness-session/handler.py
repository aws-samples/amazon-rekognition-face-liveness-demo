import boto3
from logging import Logger

rek_client = boto3.client('rekognition')
logger = Logger(name='FaceLivenessLambdaFunction')

class FaceLivenessError(Exception):
    '''
    Represents an error due to Face Liveness Issue.
    '''
    pass

def create_session():
    '''
    Get liveness session.
    '''
    try:
        response = rek_client.create_face_liveness_session()
        session_id = response.get("SessionId")
      
        return session_id
    
    except rek_client.exceptions.AccessDeniedException:
        logger.error('Access Denied Error')
        raise FaceLivenessError('AccessDeniedError')
    except rek_client.exceptions.InternalServerError:
        logger.error('InternalServerError')
        raise FaceLivenessError('InternalServerError')
    except rek_client.exceptions.InvalidParameterException:
        logger.error('InvalidParameterException')
        raise FaceLivenessError('InvalidParameterException')
    except rek_client.exceptions.ThrottlingException:
        logger.error('ThrottlingException')
        raise FaceLivenessError('ThrottlingException')
    except rek_client.exceptions.ProvisionedThroughputExceededException:
        logger.error('ProvisionedThroughputExceededException')
        raise FaceLivenessError('ProvisionedThroughputExceededException')
        
def lambda_handler(event, context):
    '''
    Main function handler.
    '''
    return {
        'statusCode': 200,
        'sessionId': create_session()
    }

if __name__ == "__main__":
    create_session()