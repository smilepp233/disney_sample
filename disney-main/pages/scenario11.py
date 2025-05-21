# disney_scenario2.py
import streamlit as st
from config.disney_scenario_template import create_disney_scenario_page


def main():
    custom_star_rating = 1.5  # 自定义星级评分值 (0.0-5.0)
    custom_rating_count = 12  # 自定义评分人数 (以K为单位，例如150.5表示150,500人)
    custom_level_confidence = 8
    survey_href = "https://hkbu.questionpro.com/t/AVqakZ59AR"  # 替换为实际的调查链接
    # 使用自定义值调用创建页面函数
    create_disney_scenario_page(
        scenario_num=11,
        custom_star_rating=custom_star_rating,
        custom_rating_count=custom_rating_count,
        survey_href=survey_href,
        custom_level_confidence=custom_level_confidence
    )


if __name__ == "__main__":
    main()
