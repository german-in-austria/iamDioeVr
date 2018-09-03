// https://eslint.org/docs/user-guide/configuring

module.exports = {
	root: true,
	parserOptions: {
		parser: "babel-eslint"
	},
	env: {
		browser: true,
	},
	extends: [
		// https://github.com/standard/standard/blob/master/docs/RULES-en.md
		'plugin:vue/base',
		'standard'
	],
	// required to lint *.vue files
	plugins: [
		'vue'
	],
	// add your custom rules here
	rules: {
		// allow paren-less arrow functions
		'arrow-parens': 0,
		// allow async-await
		'generator-star-spacing': 0,
		// allow tabs
		'no-tabs': 0,
		'indent': 0,
		'operator-linebreak': ['error', 'before'],
		'no-undef-init': 0,
		'comma-dangle': 0,
		// allow debugger during development
		'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
	}
}
