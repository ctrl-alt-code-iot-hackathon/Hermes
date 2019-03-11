var otpGenerator = require('otp-generator')
 
var otp = otpGenerator.generate(6, { upperCase: false, specialChars: false });
console.log(otp);