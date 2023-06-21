import './App.css';
import React from "react";
import { Auth } from 'aws-amplify';
import { ThemeProvider } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import FaceLiveness from './Components/FaceLiveness';
import ReferenceImage from './Components/ReferenceImage';
import {
  View,
  Flex,
} from '@aws-amplify/ui-react';


Auth.configure({
  "Auth": {
    "identityPoolId": process.env.REACT_APP_IDENTITYPOOL_ID,
    "region": process.env.REACT_APP_REGION,
    "userPoolId": process.env.REACT_APP_USERPOOL_ID,
    "mandatorySignIn": false,
    "userPoolWebClientId": process.env.REACT_APP_WEBCLIENT_ID
    // "identityPoolId": "us-east-1:70334816-9f51-47c3-b331-8e9aec04ddd9",
    // "region": "us-east-1",
    // "userPoolId": "us-east-1_YGkclllZI",
    // "mandatorySignIn": false,
    // "userPoolWebClientId": "o7f5qcifacde1edfm0ompvrs4"
  }
})



function App() {

  const [faceLivenessAnalysis, setFaceLivenessAnalysis] = React.useState(null)

  const getfaceLivenessAnalysis = (faceLivenessAnalysis) => {
    if (faceLivenessAnalysis !== null) {
      setFaceLivenessAnalysis(faceLivenessAnalysis)
    }
  }

  const tryagain = () =>{
    setFaceLivenessAnalysis(null)
  }


  return (
    <ThemeProvider>
      <Flex
        direction="row"
        justifyContent="center"
        alignItems="center"
        alignContent="flex-start"
        wrap="nowrap"
        gap="1rem"
      >
        <View
          as="div"
          maxHeight="600px"
          height="600px"
          width="740px"
          maxWidth="740px"
        >
          {faceLivenessAnalysis && faceLivenessAnalysis.Confidence ? (
            <ReferenceImage faceLivenessAnalysis={faceLivenessAnalysis} tryagain={tryagain}></ReferenceImage>
          ) :
            (<FaceLiveness faceLivenessAnalysis={getfaceLivenessAnalysis} />)}

        </View>
      </Flex>
    </ThemeProvider>


  );
}

export default App;
