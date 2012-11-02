# -*- encoding: utf-8 -*-
from decimal import Decimal

class AmountError(Exception):
    pass

class Amount:

    unity = [
        None,
        u"jeden",
        u"dwa",
        u"trzy",
        u"cztery",
        u"pięć",
        u"sześć",
        u"siedem",
        u"osiem",
        u"dziewięć",
        u"dziesięć",
        u"jedenaście",
        u"dwanaście",
        u"trzynaście",
        u"czternaście",
        u"piętnaście",
        u"szesnaście",
        u"siedemnaście",
        u"osiemnaście",
        u"dziewiętnaście"
    ]
    tens = [
        None,
        u"dziesięć",
        u"dwadzieścia",
        u"trzydzieści",
        u"czterdzieści",
        u"pięćdziesiąt",
        u"sześćdziesiąt",
        u"siedemdziesiąt",
        u"osiemdziesiąt",
        u"dziewięćdziesiąt"
    ]
    hundreds = [
        None,
        u"sto",
        u"dwieście",
        u"trzysta",
        u"czterysta",
        u"pięćset",
        u"sześćset",
        u"siedemset",
        u"osiemset",
        u"dziewięćset"
    ]

    number_suffix = [
        None,
        [u"tysiąc", u"tysiące", u"tysięcy"],
        [u"milion", u"miliony", u"milionów"],
        [u'bilion', u'biliony', u'bilionów'],
        [u'biliard', u'biliardy', u'biliardów'],
        [u'trylion', u'tryliony', u'trylionów'],
    ]

    currency = {
        'penny': [
            u"grosz",
            u"grosze",
            u"groszy"
        ],
        'buck': [
           u"złoty",
           u"złote",
           u"złotych"
        ]
    }

    @classmethod
    def in_words(cls, amount):
        amount = Decimal(amount)
        amount_parts = {'buck': int(amount//1), 'penny': int(amount%1 * 100)}

        if amount_parts['buck'] >= 10**18:
            raise AmountError("Too big amount value")

        amount_in_words = []
        for part in amount_parts:
            amount_part = str(amount_parts[part])
            in_words_list = []
            suffix_index = 0
            trinities = [amount_part[i-3 if i-3 > 0 else 0:i].zfill(3) for i in range(len(amount_part), 0, -3)]
            for trinity in trinities:
                trinity_in_words = []
                if int(trinity[0]):
                    trinity_in_words.append(cls.hundreds[int(trinity[0])])
                if int(trinity[1]) == 1:
                    trinity_in_words.append(cls.unity[int(trinity[1:3])])
                else:
                    if int(trinity[1]):
                        trinity_in_words.append(cls.tens[int(trinity[1])])
                    if int(trinity[2]):
                        trinity_in_words.append(cls.unity[int(trinity[2])])

                suffix_variety = 0
                if int(trinity) > 1:
                    suffix_variety = 1 if int(trinity[2]) in range(2, 5) and int(trinity[1]) != 1 else 2

                if suffix_index and int(trinity):
                    trinity_in_words.append(cls.number_suffix[suffix_index][suffix_variety])
                if any(trinity_in_words):
                    in_words_list.append(' '.join(trinity_in_words))
                suffix_index += 1

            in_words_list.reverse()

            currency_variety = 2 if not int(trinities[0]) else 0
            if int(trinities[0]) > 1:
                currency_variety = 1 if int(trinities[0][2]) in range(2, 5) and int(trinities[0][1]) != 1 else 2

            if int(amount_part):
                amount_in_words.append(u"%s %s" % (' '.join(in_words_list), cls.currency[part][currency_variety]))

        amount_in_words = u' i '.join(amount_in_words)

        return amount_in_words
