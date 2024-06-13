module.exports = {
  extends: ['google', 'plugin:prettier/recommended'],
  plugins: ['prettier'],
  rules: {
    'prettier/prettier': 'error',
    'require-jsdoc': 'off',
  },
};
