import requests

response = requests.get('https://xkcd.com/353/')
print(response)

##Output
# <Response [200]>

##If we want to know what we can do with response.
print(dir(response))

##Output
# ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', 
# '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', 
# '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
# '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', 
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', 
# '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 
# 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 
# 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

##To get the information in text formation
print(response.text)

##Output
##An HTML type page is displayed :
# <Response [200]>
# <!DOCTYPE html>
# <html>
# <head>
# <link rel="stylesheet" type="text/css" href="/s/7d94e0.css" title="Default"/>
# <title>xkcd: Python</title>
# <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
# <link rel="shortcut icon" href="/s/919f27.ico" type="image/x-icon"/>
# <link rel="icon" href="/s/919f27.ico" type="image/x-icon"/>
# <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml"/>
# <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml"/>
# <!-- <script type="text/javascript" src="/s/b66ed7.js" async></script>
# <script type="text/javascript" src="/s/1b9456.js" async></script> -->

# <meta property="og:site_name" content="xkcd">

# <meta property="og:title" content="Python">
# <meta property="og:url" content="https://xkcd.com/353/">
# <meta property="og:image" content="https://imgs.xkcd.com/comics/">
# <meta name="twitter:card" content="summary_large_image">

# </head>
# <body>
# <div id="topContainer">
# <div id="topLeft">
# <ul>
# <li><a href="/archive">Archive</a></li>
# <li><a href="https://what-if.xkcd.com">What If?</a></li>
# <li><a rel="author" href="/about">About</a></li>
# <li><a href="/atom.xml">Feed</a>&bull;<a href="/newsletter/">Email</a></li>
# <li><a href="https://twitter.com/xkcd/">TW</a>&bull;<a href="https://www.facebook.com/TheXKCD/">FB</a>&bull;<a href="https://www.instagram.com/xkcd/">IG</a></li>
# <li><a href="/books/">-Books-</a></li>
# <li><a href="/what-if-2/">What If? 2</a></li>
# <li><a href="/what-if/">WI?</a>&bull;<a href="/thing-explainer/">TE</a>&bull;<a href="/how-to/">HT</a></li>
# </ul>
# </div>
# <div id="topRight">
# <div id="masthead">
# <span><a href="/"><img src="/s/0b7742.png" alt="xkcd.com logo" height="83" width="185"/></a></span>
# <span id="slogan">A webcomic of romance,<br/> sarcasm, math, and language.</span>
# </div>
# <div id="news">
# <div id="xkcdNews">
# <div id="countdown" style="float: right; margin-right: 25px; width: 160px; height: 100px; position: relative;"><a style="display: flex;" href="https://xkcd.com/what-if-2/"><img alt="" style="width: 160px; height: 100px;" src="https://xkcd.com/s/5bef6b.png"><span style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); padding: 0px 8px; color: black; font-family: xkcd-Regular-v3; font-size: 20px; font-variant: small-caps; letter-spacing: 1px; white-space: nowrap; background: white none repeat scroll 0% 0%; border-radius: 99px; display: none;"></span></a></div>
# </div>
# <script>
# var client = new XMLHttpRequest();
# client.open("GET", "//c.xkcd.com/xkcd/news", true);
# client.send();
# client.onreadystatechange = function() {
#   if(client.readyState == 4 && client.status == 200) {
#     document.getElementById("xkcdNews").innerHTML = client.responseText;
#   }
# }
# </script>

# </div>
# </div>
# <div id="bgLeft" class="bg box"></div>
# <div id="bgRight" class="bg box"></div>
# </div>
# <div id="middleContainer" class="box">

# <div id="ctitle">Python</div>
# <ul class="comicNav">
# <li><a href="/1/">|&lt;</a></li>
# <li><a rel="prev" href="/352/" accesskey="p">&lt; Prev</a></li>
# <li><a href="//c.xkcd.com/random/comic/">Random</a></li>
# <li><a rel="next" href="/354/" accesskey="n">Next &gt;</a></li>
# <li><a href="/">&gt;|</a></li>
# </ul>
# <div id="comic">
# <img src="//imgs.xkcd.com/comics/python.png" title="I wrote 20 short programs in Python yesterday.  It was wonderful.  Perl, I&#39;m leaving you." alt="Python"  style="image-orientation:none" />
# </div>
# <ul class="comicNav">
# <li><a href="/1/">|&lt;</a></li>
# <li><a rel="prev" href="/352/" accesskey="p">&lt; Prev</a></li>
# <li><a href="//c.xkcd.com/random/comic/">Random</a></li>
# <li><a rel="next" href="/354/" accesskey="n">Next &gt;</a></li>
# <li><a href="/">&gt;|</a></li>
# </ul>
# <br />
# Permanent link to this comic: <a href="https://xkcd.com/353">https://xkcd.com/353/</a><br />
# Image URL (for hotlinking/embedding): <a href= "https://imgs.xkcd.com/comics/python.png">https://imgs.xkcd.com/comics/python.png</a>

# <div id="transcript" style="display: none">[[ Guy 1 is talking to Guy 2, who is floating in the sky ]]
# Guy 1: You&#39;re flying! How?
# Guy 2: Python!
# Guy 2: I learned it last night! Everything is so simple!
# Guy 2: Hello world is just &#39;print &quot;Hello, World!&quot; &#39;
# Guy 1: I dunno... Dynamic typing? Whitespace?
# Guy 2: Come join us! Programming is fun again! It&#39;s a whole new world up here!
# Guy 1: But how are you flying?
# Guy 2: I just typed &#39;import antigravity&#39;
# Guy 1: That&#39;s it?
# Guy 2: ...I also sampled everything in the medicine cabinet for comparison.
# Guy 2: But i think this is the python.
# {{ I wrote 20 short programs in Python yesterday.  It was wonderful.  Perl, I&#39;m leaving you. }}</div>
# </div>
# <div id="bottom" class="box">
# <img src="//imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap="#comicmap"/>
# <map id="comicmap" name="comicmap">
# <area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups"/>
# <area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram"/>
# <area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum"/>
# <area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description"/>
# <area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution"/>
# </map>
# <br />
# <a href="//xkcd.com/1732/"><img border=0 src="//imgs.xkcd.com/s/temperature.png" width="520" height="100" alt="Earth temperature timeline"></a>
# <br />
# <div>
# <!--
# Search comic titles and transcripts:
# <script type="text/javascript" src="//www.google.com/jsapi"></script>
# <script type="text/javascript">google.load('search', '1');google.setOnLoadCallback(function() {google.search.CustomSearchControl.attachAutoCompletion('012652707207066138651:zudjtuwe28q',document.getElementById('q'),'cse-search-box');});</script>
# <form action="//www.google.com/cse" id="cse-search-box">
# <div>
# <input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q"/>
# <input type="hidden" name="ie" value="UTF-8"/>
# <input type="text" name="q" id="q" size="31"/>
# <input type="submit" name="sa" value="Search"/>
# </div>
# </form>
# <script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&amp;lang=en"></script>
# -->
# <a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a> - <a href="/newsletter/">Email</a>
# </div>
# <br />
# <div id="comicLinks">
# Comics I enjoy:<br/>
#         <a href="http://threewordphrase.com/">Three Word Phrase</a>,
#         <a href="https://www.smbc-comics.com/">SMBC</a>,
#         <a href="https://www.qwantz.com">Dinosaur Comics</a>,
#         <a href="https://oglaf.com/">Oglaf</a> (nsfw),
#         <a href="https://www.asofterworld.com">A Softer World</a>,
#         <a href="https://buttersafe.com/">Buttersafe</a>,
#         <a href="https://pbfcomics.com/">Perry Bible Fellowship</a>,
#         <a href="https://questionablecontent.net/">Questionable Content</a>,
#         <a href="http://www.buttercupfestival.com/">Buttercup Festival</a>,
#         <a href="https://www.homestuck.com/">Homestuck</a>,
#         <a href="https://www.jspowerhour.com/">Junior Scientist Power Hour</a>
# </div>
# <br />
# <div id="comicLinks">
# Other things:<br/>
#         <a href="https://medium.com/civic-tech-thoughts-from-joshdata/so-you-want-to-reform-democracy-7f3b1ef10597">Tips on technology and government</a>,<br />
#         <a href="https://www.nytimes.com/interactive/2017/climate/what-is-climate-change.html">Climate FAQ</a>,
#         <a href="https://twitter.com/KHayhoe">Katharine Hayhoe</a>
# </div>
# <br />
# <center>
# <div id="footnote" style="width:70%">xkcd.com is best viewed with Netscape Navigator 4.0 or below on a Pentium 3&plusmn;1 emulated in Javascript on an Apple IIGS<br />at a screen resolution of 1024x1. Please enable your ad blockers, disable high-heat drying, and remove your device<br />from Airplane Mode and set it to Boat Mode. For security reasons, please leave caps lock on while browsing.</div>
# </center>
# <div id="licenseText">
# <p>
# This work is licensed under a
# <a href="https://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>.
# </p><p>
# </body><!-- Layout by Ian Clasbey, davean, and chromakode -->
# </html>
