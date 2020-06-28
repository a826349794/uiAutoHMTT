import page
from base.base import Base


class PageMpLogin(Base):

    # 1. 输入手机号
    def page_input_phone(self,phone):
        self.base_input(page.mp_phone,phone)

    # 2.输入验证码
    def page_input_code(self,code):
        self.base_input(page.mp_code,code)

    # 3.点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 4.获取昵称
    def page_get_nickname(self):
       return self.base_get_text(page.mp_nickname)

    # 5.组合登录(测试业务层调用)
    def page_mp_login(self,phone,code):
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()


