from collections import namedtuple
from hazm import Normalizer

normalizer = Normalizer()

FSItems = namedtuple("FSItems", ["income_statements", "balance_sheet"])

income_statements = {
    "درآمدهای عملیاتی": "revenue",
    "بهاى تمام شده درآمدهای عملیاتی": "cost_of_goods_sold",
    "سود (زيان) ناخالص": "gross_profit",
    "هزينه‏‌هاى فروش، ادارى و عمومى": "sales_general_and_administrative_expense",
    "هزينه‏ هاى فروش، ادارى و عمومى": "sales_general_and_administrative_expense",
    "هزینه کاهش ارزش دریافتنی‌‏ها (هزینه استثنایی)": "cost_of_decrease_in_receivables_value(exceptional_cost)",
    "هزينه کاهش ارزش دريافتني‏ ها (هزينه استثنايي)": "cost_of_decrease_in_receivables_value(exceptional_cost)",
    "ساير درآمدها": "other_operating_revenue",
    "سایر هزینه‌ها": "other_operating_expenses",
    "سود (زيان) عملياتي": "operating_income",
    "هزينه‏‌هاى مالى": "finance_expense",
    "هزينه‏ هاى مالى": "finance_expense",
    "ساير درآمدها و هزينه ‏هاى غيرعملياتى": "net_miscellaneous_revenue",
    "سایر درآمدها و هزینه‌های غیرعملیاتی- درآمد سرمایه‌گذاری‌ها": "net_miscellaneous_revenue",
    "سایر درآمدها و هزینه‌های غیرعملیاتی- اقلام متفرقه": "net_miscellaneous_revenue",
    "سود (زيان) عمليات در حال تداوم قبل از ماليات": "net_income_from_continuing_operations_before_tax",
    "سال جاری": "taxes",
    "سال‌های قبل": "taxes",
    "سود (زيان) خالص عمليات در حال تداوم": "net_income_from_continuing_operation",
    "سود (زیان) خالص عملیات متوقف شده": "discontinued_operations_profit",
    "سود (زيان) خالص عمليات متوقف شده": "discontinued_operations_profit",
    "سود (زيان) خالص": "net_income",
    "سود (زیان) خالص هر سهم– ریال": "earning_per_share",
    "سود (زيان) خالص هر سهم – ريال": "earning_per_share",
    "سرمایه": "listed_capital",
    # -------------------------------
    "بهای تمام \u200cشده درآمدهای عملیاتی": "cost_of_goods_sold",
    "سود (زیان) ناخالص": "gross_profit",
    "هزینه\u200cهای فروش، اداری و عمومی": "sales_general_and_administrative_expense",
    "سایر درآمدهای عملیاتی": "other_operating_revenue",
    "سایر هزینه\u200cهای عملیاتی": "other_operating_expenses",
    "سود (زیان) عملیاتی": "operating_income",
    "هزینه\u200cهای مالی": "finance_expense",
    "هزینه‏‌های مالی": "finance_expense",
    "سایر درآمدها و هزینه\u200cهای غیرعملیاتی- درآمد سرمایه\u200cگذاری\u200cها": "net_miscellaneous_revenue",
    "سود (زیان) عملیات در حال تداوم قبل از مالیات": "net_income_from_continuing_operations_before_tax",
    "مالیات بر درآمد": "taxes",
    "سود (زیان) خالص عملیات در حال تداوم": "net_income_from_continuing_operation",
    "سود (زیان) عملیات متوقف \u200cشده پس از اثر مالیاتی": "discontinued_operations_profit",
    "سود (زیان) خالص": "net_income",
    "سود (زیان) خالص هر سهم– ریال": "earning_per_share",
}

balance_sheet = {
    "دارايي‌هاي ثابت مشهود": "tangible_fixed_assets",
    "سرمايه‌گذاري در املاک": "investment_property",
    "دارایی‌های نامشهود": "intangible_assets",
    "سرمایه‌گذاری‌های بلندمدت": "long_term_investments",
    "دريافتني‌هاي بلندمدت": "long_term_receivables",
    "سایر دارایی‌ها": "other_assets",
    "جمع دارايي‌هاي غيرجاري": "total_non_current_assets",
    "سفارشات و پیش‌پرداخت‌ها": "prepayments",
    "موجودی مواد و کالا": "inventories",
    "دریافتنی‌های تجاری و سایر دریافتنی‌ها": "trade_and_other_receivables",
    "سرمایه‌گذاری‌های کوتاه‌مدت": "short_term_investments",
    "موجودی نقد": "cash_and_equivalents",
    "دارایی‌های نگهداری شده برای فروش": "asset_for_sale",
    "جمع دارایی‌های جاری": "total_current_assets",
    "جمع دارایی‌ها": "total_assets",
    "سرمايه": "common_stock",
    "افزایش سرمایه در جریان": "received_for_capital_advance",
    "صرف سهام": "capital_surplus",
    "صرف سهام خزانه": "treasury_stock_surplus",
    "اندوخته قانونی": "legal_reserve",
    "ساير اندوخته‌ها": "expansion_reserve",
    "مازاد تجدیدارزيابی دارایی‌ها": "revaluation_surplus",
    "تفاوت تسعیر ارز عملیات خارجی": "exchange_differences_on_translation",
    "سود (زيان) انباشته": "retained_earnings",
    "سهام خزانه": "treasury_stock",
    "جمع حقوق مالکانه": "total_shareholders_equity",
    "پرداختنی‌های بلندمدت": "long_term_liabilities",
    "تسهیلات مالی بلندمدت": "long_term_debt",
    "ذخیره مزایای پایان خدمت کارکنان": "allowance_for_post_retirement",
    "جمع بدهی‌های غیرجاری": "total_non_current_liabilities",
    "پرداختنی‌های تجاری و سایر پرداختنی‌ها": "trade_and_other_liabilities",
    "مالیات پرداختنی": "deferred_tax_liabilities",
    "سود سهام پرداختنی": "dividends_payable",
    "تسهیلات مالی": "loan_payable",
    "ذخایر": "provisions",
    "پیش‌دریافت‌ها": "deferred_revenue",
    "بدهی‌های ‌مرتبط ‌با دارایی‌های نگهداری‌‌شده برای ‌فروش": "liabilities_related_to_assets_for_sale",
    "جمع بدهی‌های جاری": "total_current_liabilities",
    "جمع بدهی‌ها": "total_liabilities",
    "جمع حقوق مالکانه و بدهی‌ها": "total_liabilities_and_shareholders_equities",
    # ---------------
    "دارایی‌های ثابت مشهود": "tangible_fixed_assets",
    "سرمایه‌گذاری در املاک": "investment_property",
    "دریافتنی‌‌های بلندمدت": "long_term_receivables",
    "پیش پرداخت‌ها و سفارشات": "prepayments",
    "دریافتنی‌‌های تجاری": "trade_and_other_receivables",
    "دریافتنی‌‌های غیرتجاری": "trade_and_other_receivables",
    "سرمایه‌گذاری‌‌های کوتاه مدت": "short_term_investments",
    "سرمایه": "common_stock",
    "افزایش (کاهش) سرمایه در جریان": "received_for_capital_advance",
    "صرف (کسر) سهام": "capital_surplus",
    "سایر اندوخته‌ها": "expansion_reserve",
    "مازاد تجدید ارزیابی دارایی‌های نگهداری شده برای فروش": "revaluation_surplus",
    "مازاد تجدید ارزیابی دارایی‌ها": "revaluation_surplus",
    "تفاوت تسعیر ناشی از تبدیل به واحد پول گزارشگری": "exchange_differences_on_translation",
    "اندوخته تسعیر ارز دارایی‌ها و بدهی‌های شرکت‌های دولتی": "exchange_differences_on_translation",
    "سود (زیان) انباشته": "retained_earnings",
    "جمع حقوق صاحبان سهام": "total_shareholders_equity",
    "پیش‌دریافت‌های غیرجاری": "long_term_liabilities",
    "پرداختنی‌های تجاری": "trade_and_other_liabilities",
    "پرداختنی‌های غیرتجاری": "trade_and_other_liabilities",
    "پیش‌دریافت‌های جاری": "deferred_revenue",
    "بدهی‌های مرتبط با دارایی‌های نگهداری شده برای فروش": "liabilities_related_to_assets_for_sale",
    "جمع بدهی‌ها و حقوق صاحبان سهام": "total_liabilities_and_shareholders_equities",
}


def normalize_key(dict_: dict):
    return {normalizer.normalize(key): val for key, val in dict_.items()}


fs_items = FSItems(
    income_statements=normalize_key(income_statements),
    balance_sheet=normalize_key(balance_sheet),
)