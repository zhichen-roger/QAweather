__author__ = "Huzhichen"
#coding=utf-8
import json
from py2neo import Graph, Node, Relationship, cypher, NodeMatcher, RelationshipMatcher

graph = Graph("http://localhost:7474", auth=("neo4j", "admin"))
matcher = NodeMatcher(graph)
# 查询节点预警
blue=matcher.match('蓝色预警').where("_.name='暴雨蓝色预警'").first()
# node=matcher.get(45)
# print(node)
print(blue)
ret = graph.run('MATCH p=(n:`蓝色预警`{name:"暴雨蓝色预警"})-[*]->(m:`学校`) return m').data()
nodesStr = json.dumps(ret[0]['m'], ensure_ascii = False)
nodes = json.loads(nodesStr)
print(nodes['content'])
nodesStr = json.dumps(blue, ensure_ascii = False)
nodes = json.loads(nodesStr)
print(nodes['name'])
# 输出边
lists=list(    graph.match(   (blue,))   )
print(lists)
