import smtplib
from email.mime.multipart import MIMEMultipart
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from catalog import models as m


def send_email(to_email, order_id):
    # get order
    order = m.Order.objects.get(id=order_id)
    # for gmail server
    server = smtplib.SMTP('mail.familymusic.me')
    server.ehlo()
    server.login('fomo@familymusic.me', 'Ganderson1')

    msg = MIMEMultipart()

    # body as html
    top = """\<html> <body style="text-align: center; background-color: rgba(255, 218, 160, .25); padding: 50px 0;"> <h1 style="text-align: center">Thank You!</h1> <p style="text-align: center"> Your order is being processed, and will be shipped to you shortly. Here is your receipt. </p> <div style="text-align: center; margin: 0 auto;"> <table style="margin-left: auto; margin-right: auto; border: solid; border-color: #dddbd7; background-color: #dddbd7; text-align: center;"> <thead> <tr style="background-color: #fff;"> <th style="padding: 5px">Image</th> <th style="padding: 5px"> Product </th> <th style="padding: 5px"> Quantity </th> <th style="padding: 5px"> Price </th> <th style="padding: 5px"> Item Total </th> </tr> </thead> <tbody>"""
    body = ""
    for item in order.active_items(include_tax_item=False):
        product = m.Product.objects.get(id=item.product.id)
        body += """\<tr> <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> <img src={} alt="Product Image" style="width: 100px" /> </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> {} </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> {} </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> ${} </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;">${}</td></tr>""".format(product.image_url(), product.name, item.quantity, item.price, item.price*item.quantity)
    bottom = """\</tbody> <tfoot> <tr style="background-color: #fff;"> <th> Sales Tax: </th> <th> </th> <th> </th> <th> </th> <th> ${} </th> </tr> <tr style="background-color: #fff;"> <th> Total: </th> <th> </th> <th> </th> <th> </th> <th> ${} </th> </tr> </tfoot> </table> </div> <p style="text-align: center"> Please let us know if you have any questions or concerns. </p> <p style="text-align: center"> Family Oriented Music Organization <br /> (801) 950-4232 <br /> sales@familymusic.me </p> <body></html>""".format(10000, order.total_price)

    html = top + body + bottom

    msg.attach(MIMEText(html, "html"))

    msg["Subject"] = "Receipt for Order ID: {}".format(str(order_id))
    msg["From"] = "fomo@familymusic.me"
    msg["To"] = to_email

    # attach file
    # f = "html.pdf"
    # with open(f, "rb") as fil:
    #     part = MIMEApplication(
    #         fil.read(),
    #         Name=basename(f)
    #     )
    # part["Content-Disposition"] = "attachment; filename=%s" % basename(f)
    # msg.attach(part)

    # send
    server.send_message(msg)

    # end
    server.quit()
