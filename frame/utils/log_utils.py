# ��־����
import logging

# ����loggerʵ��
logger = logging.getLogger('simple_example')
# ������־����
logger.setLevel(logging.DEBUG)
# ��������
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# ��־��ӡ��ʽ
formatter = logging.Formatter \
    ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ��Ӹ�ʽ����
ch.setFormatter(formatter)
# �����־����
logger.addHandler(ch)