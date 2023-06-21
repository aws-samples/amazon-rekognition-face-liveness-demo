import React from "react";
import '@aws-amplify/ui-react/styles.css';

import {
    Alert,
    Image
} from '@aws-amplify/ui-react';

function ReferenceImage({ faceLivenessAnalysis }) {
  
    return (
        <>
            <Alert
                variation="info"
                isDismissible={false}
                hasIcon={true}
            >
                Confidence Score: {faceLivenessAnalysis.Confidence.toFixed(2)}%
            </Alert>
            <Image
                src={"data:image/jpeg;base64," + faceLivenessAnalysis.ReferenceImage.Base64}
                width="100%"
                height="100%"
                objectFit="cover"
                objectPosition="50% 50%"
            />
        </>
    );
}

export default ReferenceImage;
