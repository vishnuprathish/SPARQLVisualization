#!/Users/vishnu/anaconda/bin/python
print "Content-type: text/html"
print """

<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>jQuery UI Accordion - Default functionality</title>
  <link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />
  <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
  <script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
  <link rel="stylesheet" href="/resources/demos/style.css" />
  <script>
  $(function() {
    $( "#accordion" ).accordion();
  });
  </script>
  
  <script>
    $(function() {
      $( "input[type=submit], a, button" )
        .button()
        .click(function( event ) {
          event.preventDefault();
        });
    });
    </script>
    
</head>

 """
import rdflib
from rdflib import plugin
import matplotlib.pyplot as plt
import networkx as nx
import time

G=nx.Graph()


plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

g = rdflib.Graph()
#time.sleep(10)


# ... add some triples to g somehow ...
g.parse("web_foaf.rdf")


#qres = g.query(
#    """SELECT DISTINCT ?aname ?bname
#       WHERE {
#          ?a foaf:knows ?b .
#          ?a foaf:name ?aname .
#          ?b foaf:name ?bname .
#       }""")
#"""
       

qres = g.query(
    """CONSTRUCT { ?aname foaf:knows ?bname }
        WHERE {
          ?a foaf:knows ?b .
          ?a foaf:name ?aname .
          ?b foaf:name ?bname .
       }
       """)


for row in qres:
    #print("%s knows %s" % row)
    #print row[0] + " isFriendsWith " + row[2]
    #print (row)
    
    G.add_node(row[0])
    G.add_node(row[2])
    G.add_edge(row[0],row[2])
    
    

dfs_edges1 = nx.dfs_preorder_nodes(G)
dfs_edges2 = G.nodes()

listE=[x for x in dfs_edges2]

print '<body>'

print '<div id="accordion">'
for node in listE:
    nearones=G.neighbors(node)
    
    print '<h3>' + node + '</h3>'
    print '<div>'
    print '<p>'
    print "Neighbours of this node: "
    for near_one in nearones:
        print "<button>" + near_one + "</button>"
    print '</p>'
    print '</div>'
    
print '</div>'

print "</body></html>"