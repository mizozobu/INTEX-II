import smtplib
from email.mime.multipart import MIMEMultipart
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from catalog import models as m
from account import models as amod


def send_email(to_email, order_id):
    # get order
    order = m.Order.objects.get(id=order_id)

    # get user
    user = amod.User.objects.get(email=order.user)

    # for gmail server
    server = smtplib.SMTP('mail.familymusic.me')
    server.ehlo()
    server.login('fomo@familymusic.me', 'Ganderson1')

    msg = MIMEMultipart()

    # body as html
    top = """<html> <body style="text-align: center; background-color: rgb(236, 232, 226); padding: 30px;"><div style="margin-left: 15%; margin-right: 15%; margin-bottom: 25px; padding: 30px; background-color: #fff; border: none; box-shadow: 20px 20px rgb(192, 199, 197); border-radius: 25px"><h1 style="margin:auto;text-align: center;padding: 15px; background-color: rgba(236, 232, 226, 1);width:70%;border-radius:20px">Family Oriented Music Organization</h1><h2 style="text-align: center">Thank You {} {}!</h2> <p style="text-align: center"> Your order is being processed, and will be shipped to you shortly. Here is your receipt. </p> <div style="text-align: center; margin: 0 auto;"> <table style="border-radius: 10px;margin-left: auto; width: 70%;margin-right: auto; border: solid; border-color: #dddbd7; background-color: #dddbd7; text-align: center;"> <thead> <tr style="background-color: #fff;"> <th style="padding: 5px"> Product </th> <th style="padding: 5px"> Quantity </th> <th style="padding: 5px"> Price </th> <th style="padding: 5px"> Item Total </th> </tr> </thead> <tbody>""".format(user.first_name, user.last_name)
    body = ""
    for item in order.active_items(include_tax_item=False):
        product = m.Product.objects.get(id=item.product.id)
        body += """<tr>
            <td style="vertical-align: middle; background-color: #fff; padding: 20px;"> {} </td>
            <td style="vertical-align: middle; background-color: #fff; padding: 20px;"> {} </td>
            <td style="vertical-align: middle; background-color: #fff; padding: 20px;"> ${} </td>
            <td style="vertical-align: middle; background-color: #fff; padding: 20px;">${}</td>
            </tr>""".format(product.name, item.quantity, item.price, (item.price*item.quantity))
    taxProd = m.Product.objects.get(name="Sales Tax")
    taxItem = order.get_item(taxProd)
    bottom = """</tbody> <tfoot> <tr style="background-color: #fff;"> <th> Sales Tax: </th> <th> </th> <th> </th> <th> ${} </th> </tr> <tr style="background-color: #fff;"> <th style="background-color: rgba(236, 232, 226, 1);"> Total: </th> <th style="background-color: rgba(236, 232, 226, 1);" > </th> <th style="background-color: rgba(236, 232, 226, 1);"> </th> <th style="background-color: rgba(236, 232, 226, 1);"> ${} </th> </tr> </tfoot> </table> </div> <p style="text-align: center"> Please let us know if you have any questions or concerns. </p> <p style="text-align: center"> Family Oriented Music Organization <br /> (801) 950-4232 <br /> fomo@familymusic.me </p></div> </body></html>""".format(taxItem.price, order.total_price)

    html = top + body + bottom

    # html = """
    #     <html>
    #       <head></head>
    #       <body style="text-align: center; background-color: rgba(255, 218, 160, .25); padding: 50px 0;">
    #         <h1 style="text-align: center">Thank You!</h1>
    #           <p style="text-align: center"> Your order is being processed, and will be shipped to you shortly. Here is your receipt.</p>
    #            <div style="text-align: center; margin: 0 auto;">
    #             <table style="margin-left: auto; margin-right: auto; border: solid; border-color: #dddbd7; background-color: #dddbd7; text-align: center;">
    #                 <thead>
    #                     <tr style="background-color: #fff;">
    #                         <th style="padding: 5px">Image</th>
    #                         <th style="padding: 5px"> Product </th>
    #                         <th style="padding: 5px"> Quantity </th>
    #                         <th style="padding: 5px"> Price </th>
    #                         <th style="padding: 5px"> Item Total </th>
    #                     </tr>
    #                 </thead>
    #
    #                 <tbody>
    #                     <tr>
    #                         <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> <img src={} alt="Product Image" style="width: 100px" /> </td>
    #                         <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> {} </td>
    #                         <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> {} </td>
    #                         <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> ${} </td>
    #                         <td style="vertical-align: middle; background-color: #fff; padding: 10px;">${}</td>
    #                     </tr>
    #                 </tbody>
    #
    #                 <tfoot>
    #                     <tr style="background-color: #fff;">
    #                         <th> Sales Tax: </th>
    #                         <th> </th>
    #                         <th> </th>
    #                         <th> </th>
    #                         <th> ${} </th>
    #                     </tr>
    #
    #                     <tr style="background-color: #fff;">
    #                         <th> Total: </th>
    #                         <th> </th>
    #                         <th> </th>
    #                         <th> </th>
    #                         <th> ${} </th>
    #                     </tr>
    #                 </tfoot>
    #             </table>
    #         </div>
    #
    #         <p style="text-align: center"> Please let us know if you have any questions or concerns. </p>
    #         <p style="text-align: center"> Family Oriented Music Organization <br> (801) 950-4232 <br> sales@familymusic.me </p>
    #         </body>
    #     </html>
    #     """"



    msg.attach(MIMEText(html, "html"))

    print("Email*************", to_email)
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

    # for item in order.active_items(include_tax_item=True):
    #     product = m.Product.objects.get(id=item.product.id)
    #     body += """\<tr> <td style="vertical-align: middle; background-color: #fff; padding: 10px;"> <img src=""" + str(product.image_url()) + """ alt="Product Image" style="width: 100px" /> </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;">""" + str(product.name) + """ </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;">""" + str(product.quantity) + """ </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;">""" + str(item.price) + """ </td> <td style="vertical-align: middle; background-color: #fff; padding: 10px;">""" + str(item.price*item.quantity) + """ </td></tr>"""
    # bottom = """\</tbody> <tfoot> <tr style="background-color: #fff;"> <th> Sales Tax: </th> <th> </th> <th> </th> <th> </th> <th> ${} </th> </tr> <tr style="background-color: #fff;"> <th> Total: </th> <th> </th> <th> </th> <th> </th> <th> ${} </th> </tr> </tfoot> </table> </div> <p style="text-align: center"> Please let us know if you have any questions or concerns. </p> <p style="text-align: center"> Family Oriented Music Organization <br /> (801) 950-4232 <br /> sales@familymusic.me </p> <body></html>""".format(10000, order.total_price)
