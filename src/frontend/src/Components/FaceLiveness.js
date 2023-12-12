import React from "react";
import { useEffect } from "react";
import { Loader } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import { FaceLivenessDetector } from '@aws-amplify/ui-react-liveness';


function FaceLiveness({faceLivenessAnalysis}) {
    const [loading, setLoading] = React.useState(true);
    const [sessionId, setSessionId] = React.useState(null)
   

    const endpoint = process.env.REACT_APP_ENV_API_URL ? process.env.REACT_APP_ENV_API_URL : ''

    useEffect(() => {
        /*
         * API call to create the Face Liveness Session
         */
        const fetchCreateLiveness = async () => {
            const response = await fetch(endpoint + 'createfacelivenesssession');
            const data = await response.json();
            setSessionId(data.sessionId)
            setLoading(false);

        };
        fetchCreateLiveness();

    },[])

    /*
   * Get the Face Liveness Session Result
   */
    const handleAnalysisComplete = async () => {
        /*
         * API call to get the Face Liveness Session result
         */
        const response = await fetch(endpoint + 'getfacelivenesssessionresults',
            {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ sessionid: sessionId })
            }

        );
        const data = await response.json();
        faceLivenessAnalysis(data.body)
    };

    return (
        <>
            {loading ? (
                <Loader />
            ) : (
                <FaceLivenessDetector
                    sessionId={sessionId}
                    region="us-east-1"
                    onAnalysisComplete={handleAnalysisComplete}
                    onError={(error) => {
                        console.error(error);
                      }}
                />
            )}
        </>
    );
}

export default FaceLiveness;
