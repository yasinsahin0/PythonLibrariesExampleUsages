import logging

logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)

logging.debug('bu mesaj log dosyasına gider.')
logging.warning('Hata mesajı') # konsola mesaj yazdırır
logging.info('bilgi mesajı') # hiç bir şey yazdırmayacak
logging.error('error mesajı')