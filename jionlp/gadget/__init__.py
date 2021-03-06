# -*- coding=utf-8 -*-


from .money_standardization import MoneyStandardization
from .split_sentence import SplitSentence
from .id_card_parser import IDCardParser
from .location_parser import LocationParser
from .location_recognizer import LocationRecognizer
from .remove_stopwords import RemoveStopwords
from .ts_conversion import TSConversion
from .pinyin import Pinyin
from .char_radical import CharRadical
from .back_translation import BackTranslation, BaiduApi, YoudaoFreeApi, \
    YoudaoApi, GoogleApi, TencentApi, XunfeiApi
from .phone_location import PhoneLocation
from .idiom_solitaire import IdiomSolitaire
from jionlp.util.fast_loader import FastLoader


money_standardization = MoneyStandardization()
parse_id_card = IDCardParser()
split_sentence = SplitSentence()
parse_location = LocationParser()
recognize_location = LocationRecognizer()
remove_stopwords = RemoveStopwords()
tra_sim_conversion = TSConversion()
tra2sim = tra_sim_conversion.tra2sim
sim2tra = tra_sim_conversion.sim2tra
pinyin = Pinyin()
idiom_solitaire = IdiomSolitaire()
char_radical = CharRadical()
phone_location = PhoneLocation()
cell_phone_location = phone_location.cell_phone_location
landline_phone_location = phone_location.landline_phone_location


# rule = FastLoader('rule', globals(), 'jionlp.rule')
del tra_sim_conversion
# del FastLoader
