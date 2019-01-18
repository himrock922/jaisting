// webpack.config.js
var path = require('path')
var BundleTracker = require('webpack-bundle-tracker')
var VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    entry: './frontend/packs/application.js',
    output: {
        path: path.resolve(__dirname, './public/bundles/'),
        filename: "[name]-[hash].js",
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new VueLoaderPlugin(),
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                include: [ // use `include` vs `exclude` to white-list vs black-list
                    path.resolve(__dirname, "node_modules"), // white-list your app source files
                    require.resolve("bootstrap-vue"), // white-list bootstrap-vue
                ],
                loader: "babel-loader"
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.vue$/,
                use: ['vue-loader']
            }
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
            'vuex$': 'vuex/dist/vuex.js'
        }
    }
}