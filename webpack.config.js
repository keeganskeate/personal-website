/*
  Module Bundler | Personal Website
  Created 4/15/2021
*/
const Dotenv = require('dotenv-webpack');
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const path = require('path');
const appName = 'personal_website';

module.exports = env => {
  return {
    mode: env.production ? 'production' : 'development',
    devtool: env.production ? 'source-map' : 'eval',
    devServer: {
      writeToDisk: true, // Write files to disk in dev mode, so that Django can serve the assets.
    },
    resolve: {
      extensions: [ '.js' ]
    },
    entry: [
      `./${appName}/assets/css/app.scss`,
      `./${appName}/assets/js/index.js`,
      // Optional: Add additional JS here.
    ],
    output: {
      path: path.resolve(__dirname, `${appName}/static/${appName}`),
      filename: './js/bundle.js',
      libraryTarget: 'var',
      library: 'app', // Turns JavaScript into a module.
    },
    module: {
      rules: [
        {
          test: /\.s?css$/,
          use: [
            {
              loader: 'file-loader', // Output CSS.
              options: {
                name: './css/bundle.css',
              },
            },
            {
              loader: 'sass-loader', // Compiles Sass to CSS.
              options: {
                implementation: require('sass'),
                webpackImporter: false,
                sassOptions: {
                  includePaths: ['./node_modules'],
                },
              },
            },
          ],
        },
        {
          test: /\.js$/,
          loader: 'babel-loader', // Convert ES2015 to JavaScript.
          query: {
            "presets": [
              ["@babel/preset-env", {
                "targets": { "esmodules": true }
              }]
            ]
          },
        },
      ],
    },
    plugins: [
      new Dotenv(), // Make .env variables available in entry file.
      new OptimizeCSSAssetsPlugin({}), // Minimize the CSS.
    ],
  }
};
