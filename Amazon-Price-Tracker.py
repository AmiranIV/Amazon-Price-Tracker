import smtplib
import lxml
import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.com/-/he/%D7%A2%D7%99%D7%A0%D7%99%D7%99%D7%9D-%D7%9E%D7%97%D7%95%D7%9E%D7%9E%D7%AA-%D7%9C%D7%A2%D7%99%D7%A0%D7%99%D7%99%D7%9D-Chalazion-Blepharitis/dp/B072KGXMQ7/ref=d_pd_sbs_sccl_2_6/132-4864670-0122551?pd_rd_w=FotBM&amp&content-id=amzn1.sym.3676f086-9496-4fd7-8490-77cf7f43f846&amp&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&amp&pf_rd_r=GAY1AZV1FJ38BT3DQHCG&amp&pd_rd_wg=f2lpk&amp&pd_rd_r=96848b1b-5508-461f-814e-90a7a44da017&amp&pd_rd_i=B072KGXMQ7&amp&psc=1&amp&language=en_US&language=he_IL&currency=USD"
header = {
    "User-Agent": "ADD Yours"
    "Accept-Language": "ADD Yours"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

#####item price######
whole = soup.find_all(name="span", class_="a-price-whole")
decimal = soup.find_all(name="span", class_="a-price-decimal")
fraction = soup.find_all(name="span", class_="a-price-fraction")
price = [whole[0].getText(), decimal[0].getText(), fraction[0].getText()]
float_item_price = float(price[0] + price[2])

####Email alert!!#####
my_email = "EMAIL"
password = "PASSWORD"

if float_item_price < 19:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="EMAIL",
                            msg=f"Subject:Item Price Alert! \n\nThe Price of the item you wanted is less then 19$ !")
