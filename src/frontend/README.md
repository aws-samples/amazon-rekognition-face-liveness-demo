# Getting Started with Create Face Liveness React App


## First create a .env.local file in the frontend directory with the following contents:

```
REACT_APP_ENV_API_URL=https://YOUR_API_GW_STAGE_URL
REACT_APP_IDENTITYPOOL_ID=AMAZON_COGNITO_IDENTITYPOOL_ID
REACT_APP_REGION=AMAZON_COGNITO_APP_REGION
REACT_APP_USERPOOL_ID=AMAZON_COGNITO_APP_USERPOOL_ID
REACT_APP_WEBCLIENT_ID=AMAZON_COGNITO_APP_WEBCLIENT_ID

```

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

