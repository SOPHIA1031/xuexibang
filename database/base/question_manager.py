# -*-coding:utf-8-*-
# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: question_manager.py
# ��ģ�������
# ������ɼ������ݿ��������

from database.models.model import QuestionInfo


def get_home_question(number, session):
    question_list = []
    res = {}
    question_info_list = session.query(QuestionInfo).limit(number).all()

    for question_info in question_info_list:
        if isinstance(question_info, QuestionInfo):
            question_list.append(question_info.to_dict())
        else:
            res["success"] = False
            res["status"] = 1000
            res["message"] = "Unknown Error"
            res["content"] = question_info_list
            return res
    res["success"] = True
    res["status"] = 0
    res["message"] = "Home question got"
    res["content"] = question_info_list
    return res
