from pages.base_page import BasePage


class LoginPage(BasePage):    
        USERNAME_INPUT="#user-name"
        PASSWORD_INPUT="#password"
        LOGIN_BUTTON="#login-button"
        ERR0R_MSG="[data-test='error']"
        
        def login(self, username: str, password: str):
            self.fill(self.USERNAME_INPUT, username)
            self.fill(self.PASSWORD_INPUT, password)
            self.click(self.LOGIN_BUTTON)
            
        def is_error_displayed(self) -> str:
            return self.get_text(self.ERR0R_MSG)
        
        def get_error_message(self) -> str:
          return self.get_text(self.ERROR_MSG)




        
        
        
   