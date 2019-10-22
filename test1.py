from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from io import BytesIO
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
url = "https://passport.zhaopin.com/org/login?bkurl=https%3A%2F%2Frd5.zhaopin.com%2Fcustom%2Fsearch%2Fresult"
BORDER = 6  #开始滑动的小块与左边缘的距离
INIT_LEFT = 60  #开始从X轴方向即x=60开始检测缺口的位置

browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath("//input[@id='username']").send_keys('isoftstone_yehan')
sleep(1)
browser.find_element_by_xpath("//input[@id='password']").send_keys("5619899.hql")
sleep(1)
browser.quit()
    # def getImagePosition(self):
    #     # 获取验证图在网页中的位置并以元组的方式返回
    #     geetestImage = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
    #     sleep(2)
    #     location = geetestImage.location
    #     size = geetestImage.size
    #     top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
    #         'width']
    #     return (top, bottom, left, right)
