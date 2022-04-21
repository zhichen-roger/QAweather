__author__ = "Huzhichen"
#coding=utf-8
import json
from py2neo import Graph, Node, Relationship, cypher, NodeMatcher, RelationshipMatcher
graph = Graph("http://localhost:7474", auth=("neo4j", "admin"))
matcher = NodeMatcher(graph)
sentence='降雨预警紫色降雨学校预防措施'
answerStence=''
if sentence.find('雨')!=-1 :
    if sentence.find('蓝色')!=-1:
        if sentence.find('措施')!=-1 or sentence.find('预防措施')!=-1 or sentence.find('方法')!=-1 or sentence.find('预防方法')!=-1 or sentence.find('防汛')!=-1:
            if sentence.find('学校')!=-1 or sentence.find('大学')!=-1 or sentence.find('本科')!=-1 or sentence.find('高中')!=-1 or sentence.find('初中')!=-1 or sentence.find('小学')!=-1 or sentence.find('小学')!=-1 or sentence.find('幼儿园')!=-1:
                ret = graph.run('MATCH p=(n:`蓝色预警`{name:"暴雨蓝色预警"})-[*]->(m:`学校`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence=nodes['content']
                print(answerStence)
            elif sentence.find('政府')!=-1:
                ret = graph.run('MATCH p=(n:`蓝色预警`{name:"暴雨蓝色预警"})-[*]->(m:`政府`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('户外人员')!=-1 or sentence.find('户外工作者')!=-1:
                ret = graph.run('MATCH p=(n:`蓝色预警`{name:"暴雨蓝色预警"})-[*]->(m:`户外人员`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('城管部门')!=-1:
                ret = graph.run('MATCH p=(n:`蓝色预警`{name:"暴雨蓝色预警"})-[*]->(m:`城管部门`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            else:
                f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
                f1.write(sentence + '\n')
                print("保存成功")
                f1.close()
                answerStence = '抱歉，我还不会，真正学习中!'
                #print(answerStence)
        elif sentence.find('降雨量')!=-1 or sentence.find('雨量')!=-1:
            ret = graph.run('MATCH p=(n:`蓝色预警`{name:"暴雨蓝色预警"})-[*]->(m:`级别标准`) return m').data()
            nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
            nodes = json.loads(nodesStr)
            answerStence = nodes['name']
            print(answerStence)
        else:
            f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
            f1.write(sentence + '\n')
            print("保存成功")
            f1.close()
            answerStence = '抱歉，我还不会，真正学习中!'
            #print(answerStence)
    elif sentence.find('黄色')!=-1:
        if sentence.find('措施') != -1 or sentence.find('预防措施') != -1 or sentence.find('方法') != -1 or sentence.find('预防方法') != -1 or sentence.find('防汛') != -1:
            if sentence.find('学校') != -1 or sentence.find('大学') != -1 or sentence.find('本科') != -1 or sentence.find('高中') != -1 or sentence.find('初中') != -1 or sentence.find('小学') != -1 or sentence.find('小学') != -1 or sentence.find('幼儿园') != -1:
                ret = graph.run('MATCH p=(n:`黄色预警`{name:"暴雨黄色预警"})-[*]->(m:`学校`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('政府') != -1:
                ret = graph.run('MATCH p=(n:`黄色预警`{name:"暴雨黄色预警"})-[*]->(m:`政府`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('户外人员') != -1 or sentence.find('户外工作者') != -1:
                ret = graph.run('MATCH p=(n:`黄色预警`{name:"暴雨黄色预警"})-[*]->(m:`户外人员`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('城管部门') != -1:
                ret = graph.run('MATCH p=(n:`黄色预警`{name:"暴雨黄色预警"})-[*]->(m:`城管部门`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            else:
                f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
                f1.write(sentence + '\n')
                print("保存成功")
                f1.close()
                answerStence = '抱歉，我还不会，真正学习中!'
                #print(answerStence)
        elif sentence.find('降雨量')!=-1 or sentence.find('雨量')!=-1:
            ret = graph.run('MATCH p=(n:`黄色预警`{name:"暴雨黄色预警"})-[*]->(m:`级别标准`) return m').data()
            nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
            nodes = json.loads(nodesStr)
            answerStence = nodes['name']
            print(answerStence)
        else:
            f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
            f1.write(sentence + '\n')
            print("保存成功")
            f1.close()
            answerStence = '抱歉，我还不会，真正学习中!'
            #print(answerStence)
    elif sentence.find('橙色')!=-1:
        if sentence.find('措施') != -1 or sentence.find('预防措施') != -1 or sentence.find('方法') != -1 or sentence.find('预防方法') != -1 or sentence.find('防汛') != -1:
            if sentence.find('学校') != -1 or sentence.find('大学') != -1 or sentence.find('本科') != -1 or sentence.find('高中') != -1 or sentence.find('初中') != -1 or sentence.find('小学') != -1 or sentence.find('小学') != -1 or sentence.find('幼儿园') != -1:
                ret = graph.run('MATCH p=(n:`橙色预警`{name:"暴雨橙色预警"})-[*]->(m:`学校`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('政府') != -1:
                ret = graph.run('MATCH p=(n:`橙色预警`{name:"暴雨橙色预警"})-[*]->(m:`政府`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('户外人员') != -1 or sentence.find('户外工作者') != -1:
                ret = graph.run('MATCH p=(n:`橙色预警`{name:"暴雨橙色预警"})-[*]->(m:`户外人员`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('城管部门') != -1:
                ret = graph.run('MATCH p=(n:`橙色预警`{name:"暴雨橙色预警"})-[*]->(m:`城管部门`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            else:
                f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
                f1.write(sentence + '\n')
                print("保存成功")
                f1.close()
                answerStence = '抱歉，我还不会，真正学习中!'
                #print(answerStence)
        elif sentence.find('降雨量')!=-1 or sentence.find('雨量')!=-1:
            ret = graph.run('MATCH p=(n:`橙色预警`{name:"暴雨橙色预警"})-[*]->(m:`级别标准`) return m').data()
            nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
            nodes = json.loads(nodesStr)
            answerStence = nodes['name']
            print(answerStence)
        else:
            f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
            f1.write(sentence + '\n')
            print("保存成功")
            f1.close()
            answerStence = '抱歉，我还不会，真正学习中!'
            #print(answerStence)
    elif sentence.find('红色')!=-1:
        if sentence.find('措施') != -1 or sentence.find('预防措施') != -1 or sentence.find('方法') != -1 or sentence.find('预防方法') != -1 or sentence.find('防汛') != -1:
            if sentence.find('学校') != -1 or sentence.find('大学') != -1 or sentence.find('本科') != -1 or sentence.find('高中') != -1 or sentence.find('初中') != -1 or sentence.find('小学') != -1 or sentence.find('小学') != -1 or sentence.find('幼儿园') != -1:
                ret = graph.run('MATCH p=(n:`红色预警`{name:"暴雨红色预警"})-[*]->(m:`学校`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('政府') != -1:
                ret = graph.run('MATCH p=(n:`红色预警`{name:"暴雨红色预警"})-[*]->(m:`政府`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            elif sentence.find('城管部门') != -1:
                ret = graph.run('MATCH p=(n:`红色预警`{name:"暴雨红色预警"})-[*]->(m:`城管部门`) return m').data()
                nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
                nodes = json.loads(nodesStr)
                answerStence = nodes['content']
                print(answerStence)
            else:
                f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
                f1.write(sentence + '\n')
                print("保存成功")
                f1.close()
                answerStence = '抱歉，我还不会，真正学习中!'
                #print(answerStence)
        elif sentence.find('降雨量')!=-1 or sentence.find('雨量')!=-1:
            ret = graph.run('MATCH p=(n:`红色预警`{name:"暴雨红色预警"})-[*]->(m:`级别标准`) return m').data()
            nodesStr = json.dumps(ret[0]['m'], ensure_ascii=False)
            nodes = json.loads(nodesStr)
            answerStence = nodes['name']
            print(answerStence)
        else:
            f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
            f1.write(sentence + '\n')
            print("保存成功")
            f1.close()
            answerStence = '抱歉，我还不会，真正学习中!'
            #print(answerStence)
    else:
        f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
        f1.write(sentence + '\n')
        print("保存成功")
        f1.close()
        answerStence = '抱歉，我还不会，真正学习中!'
else:
    f1 = open(r'/问题保存.txt', "a+", encoding='utf-8')
    f1.write(sentence + '\n')
    print("保存成功")
    f1.close()
    answerStence = '抱歉，我还不会，真正学习中!'
print(answerStence)