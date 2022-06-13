module.exports = {
    entry: './src/js/index.js',
    mode: 'development',
    output: {
        filename: 'index.js',
        path: '/Users/lriad/code/portfolio/hopsnshine/static/js'
    },
    module: {
        rules: [
            {
                test: /\.(scss)$/,
                use: ['style-loader', 'css-loader', 'sass-loader']
            }
        ]
    }
};