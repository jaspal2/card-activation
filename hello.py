import sys
import os

class tokenGenerator:
    def token(self):
        sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

        from twocaptcha import TwoCaptcha
        
        api_key = os.getenv('APIKEY_2CAPTCHA', '8be6cdc9b0bb51ec36925f6c77f33c09')
        
        solver = TwoCaptcha(api_key)
        
        try:
            result = solver.recaptcha(
                sitekey='6LcwdZ8UAAAAACzsqVmYcPjLMOXfpUZoXP2dL_HV',
                url='https://a1activate.com.au/monashuniversityactivationpage')
        
        except Exception as e:
            sys.exit(e)
        
        else:
            #sys.exit('solved: ' + str(result))
            return sys.exit(str(result))
        #sys.exit('solved: ' + str(result))
