"""
--- Day 1: Historian Hysteria ---
The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently empty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

For example:

3   4
4   3
2   5
1   3
3   9
3   3
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

In the example list above, the pairs and distances would be as follows:

The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
The third-smallest number in both lists is 3, so the distance between them is 0.
The next numbers to pair up are 3 and 4, a distance of 1.
The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?

"""


input = """53906   14872
35867   86182
61313   43656
23620   85315
96434   90834
70853   80045
81024   46279
74096   30947
95143   21374
58372   72621
31935   12389
49854   67579
86609   43656
89364   63407
74266   14457
52098   88395
96964   96234
49393   18203
50534   68865
15769   46056
80451   31396
74551   38740
91700   86211
93090   21692
17501   34796
16736   15045
46056   37224
75968   93912
97701   75324
28685   71207
51195   28531
74109   81902
61906   30947
61901   26456
27949   31935
80781   31935
45869   63848
76250   91948
92161   88896
92901   95050
84135   56554
36445   85108
91602   50652
14229   42099
26675   53544
31839   80370
79535   80370
36655   21828
68093   10740
49052   30403
38777   87413
10824   94461
38968   80370
63083   81902
95411   55634
69727   81902
93596   70536
52663   31396
65999   68564
59890   40680
66226   43656
94707   13595
13899   79022
25283   66901
79946   33564
80152   25915
78359   38273
28675   78207
51401   24017
21022   36263
96272   97201
22693   27307
21648   97487
46178   97979
17466   60051
82661   25915
39775   93045
48681   60562
47199   86686
30660   85874
18285   69937
55428   50228
98906   13151
86638   57318
48728   66727
78268   80222
32191   18625
75544   96995
38692   27814
51182   72597
24564   14872
78193   43656
14830   98087
51013   91047
40389   62018
80648   34735
25915   48415
75278   30947
73740   76891
47851   63741
30743   93960
30074   81716
47127   31935
66658   14609
81404   13612
78838   34796
98988   56858
61023   95843
44069   79751
58419   22373
88253   33943
10357   68564
65647   75968
56636   49814
96378   30947
61167   62569
34557   37250
64400   55670
51614   31935
12364   73721
71834   63350
11214   15293
84197   67580
46279   19369
85435   25099
87320   40454
28341   16142
65983   71345
94333   79356
66873   33981
50771   31396
91221   54646
63742   34796
99770   46279
37731   80045
20432   21157
39263   76136
99080   56687
29242   32173
93843   46279
53850   18085
68835   75005
43354   40124
48317   29974
89326   97201
75434   22373
70473   25915
63394   48255
38016   68564
78812   80045
93261   58244
20014   64971
11924   11780
21157   53840
24802   89474
55997   38754
87219   25915
20988   14872
39639   28428
29464   51586
61672   78802
96734   65594
55764   14925
52658   49815
66306   81902
19417   81326
20305   17693
33337   15419
58435   11780
88271   55426
72760   70448
62171   41784
35420   75968
85791   80045
86874   28578
47942   65464
65982   43656
54647   80045
76794   72117
71733   56858
99560   97201
57741   48255
19684   38234
82201   34796
56598   81902
78671   30403
57520   81902
28794   80045
70718   36673
12894   89585
80420   88896
75179   80045
37527   94333
68865   89708
54484   70184
22482   90992
28787   99580
23380   50228
24819   34018
23039   26417
34777   30403
38089   98258
40091   90301
65391   81902
64984   88288
47803   19170
54239   23050
89439   35940
64104   15601
42956   50228
60123   42357
62887   87025
50719   56858
60551   40959
32730   73652
80253   80045
31948   19369
33170   19369
43380   88896
66465   54668
68963   25915
74433   40124
42272   11349
45882   51505
62636   26196
97266   11220
23083   96587
27358   76569
44481   81623
11314   30728
64712   57329
95360   81902
43100   83387
22699   72297
95680   57279
12170   30947
51297   59853
48255   49975
23355   34796
55264   96834
43234   95736
58663   66937
24467   93318
31569   39898
91720   37056
17395   97253
87456   68460
61344   13591
50316   50228
50313   82900
33328   41831
70391   98955
40124   13612
80337   21838
66151   17628
14932   57871
34464   48255
18164   70338
84969   14872
30898   68564
76526   11873
41007   43656
46997   52069
74614   79205
97267   80045
13525   56858
83587   23900
70678   51307
96613   20308
39592   31396
44365   91747
44840   87970
99891   90134
58567   33972
58851   43402
87728   30403
84786   37227
13329   32507
93229   90123
43915   54511
83982   27814
19567   88896
33979   87294
40170   43656
97852   48739
45928   94736
74935   28466
97730   84011
74826   95244
68208   24359
53130   92198
41725   78978
57089   11780
98073   35872
23652   11780
97201   41849
87155   71818
88640   79810
37745   21157
14056   18175
95658   56858
48755   94333
13619   45286
81792   43656
78244   31396
30595   45955
84035   95996
60013   20192
30544   13612
94649   59748
12343   75968
37130   68564
89486   25915
30879   45350
82252   76332
72035   81326
96757   39307
12935   22093
76836   96648
13035   65492
64394   56858
68916   43656
81474   31396
90650   28126
56290   94702
35758   56672
58825   41199
55904   89015
39969   10888
45804   80699
39063   33732
71312   14949
98164   36727
83970   87031
63860   15740
19008   80045
36342   59349
75519   71974
70509   49833
15393   80714
98995   85760
80265   80370
95001   42793
28863   71880
65186   59896
91417   37319
18213   74991
46598   73652
17350   56836
77732   24742
43239   96665
91884   73652
98023   17915
30603   81326
50132   72240
14657   26301
89888   46056
29239   11140
33269   80370
86498   43609
32323   18944
87234   14483
91312   84354
55972   28052
95671   44209
47556   94712
64231   92523
40010   52869
78889   65874
65672   11780
66829   27274
58976   23077
52684   99212
12106   78809
40894   79813
73516   30403
98758   90245
78558   81135
91842   43656
36111   56858
81902   57457
57016   15315
62322   31642
12386   91620
46583   57818
16653   33234
90664   13612
99386   20422
53504   20328
88729   68564
33262   89807
22996   31396
49944   21157
71217   57474
89409   93464
81592   54135
98029   75431
54437   89337
73652   85178
44888   25915
16495   94354
20340   30974
69933   86157
23100   19122
27337   71603
81726   94579
36381   80370
13641   39385
93685   32550
73502   76018
95815   49303
26455   31396
89509   94333
43369   60492
78840   66925
84665   19369
27145   30682
20548   34796
51087   84227
24544   89081
72048   57058
70432   19369
66825   40124
30189   35430
87176   89952
69550   68440
52304   27404
22031   76800
41939   80370
30725   67957
71537   22373
53526   66477
65213   20836
51028   68564
87427   46945
18856   88896
12027   68564
28641   39589
49464   72751
15977   74910
58898   75990
39039   62184
67691   57314
60850   49736
13012   48255
84069   97201
32568   68865
96125   34796
25181   74948
73744   43656
56977   21157
80745   22716
68012   34796
47755   48255
78533   29915
23621   68865
11353   43088
84311   18978
88935   20794
54337   87927
62396   46248
83685   15158
13519   40474
89345   94333
91712   56672
54787   22373
41442   19369
57095   49689
73305   68074
40222   34796
18020   22841
62794   75878
26368   14901
11475   40124
75682   74145
75582   80370
97642   80045
43518   31396
61262   14872
65073   35575
64250   41578
41393   43656
43735   59876
52143   68865
20553   52835
88338   81503
92669   68564
97752   18898
30830   94320
13583   13612
34097   54600
95952   66295
20902   68564
35750   86876
79359   57300
19583   43538
77422   21157
63966   88896
25403   57385
71523   94333
93579   11780
35074   68865
75840   48255
44626   47096
72438   60433
54577   68564
66690   56858
41197   40124
13612   30497
25465   86662
55920   78165
89969   67123
58286   70389
43656   97260
82249   43755
30657   96171
39157   31396
18894   32478
11955   10307
43927   43656
16920   50228
29478   94333
77022   17632
33574   30653
52142   59421
43400   58568
20918   21157
59754   48255
54975   74539
45684   99214
70895   33500
68461   80541
96575   26109
39266   97201
85211   31396
62831   13612
58008   89741
52256   30403
67407   31396
11485   36725
73476   43656
28411   20566
58997   24742
50228   94333
22731   49787
60317   31396
50387   56858
47125   76520
32596   40699
86041   60374
17153   93396
47001   97796
95064   33317
60020   31715
97079   13537
95911   97201
42771   30403
31218   94333
58019   68797
27090   34796
42716   89943
13624   67333
14872   41803
15763   99088
59386   71716
29342   81287
85955   37265
92842   20523
84757   75968
76051   41922
27595   46689
74249   81347
76224   97201
46211   43561
16434   31396
95096   74640
65042   56672
89918   56858
57601   94333
45468   11780
38812   25915
51266   55991
90185   75968
75344   13612
68758   50890
54439   97201
49138   21157
72447   14872
24656   40124
94875   22613
22373   43361
44518   10761
43686   60879
32501   92097
42849   13612
96366   97201
97664   18585
75951   45638
87742   55727
26127   90094
49148   29249
44880   27199
48351   34429
49769   19369
53310   31313
97615   97700
44217   70925
35613   84873
37774   33414
37902   67163
20513   31396
22058   11456
69695   43656
12676   43656
78546   44430
93366   88781
43779   79593
42156   94062
26825   30947
61551   58309
79992   80045
70690   92191
60303   33345
47232   40844
27958   75524
65137   43403
81422   88896
90350   36543
82498   21157
34184   84567
49629   78699
52046   74192
68564   51586
74624   88896
84055   35652
78176   24112
19369   81326
29606   25074
56381   25915
41549   94333
98646   77958
10620   49796
71804   80045
70094   21157
22047   43771
26955   75968
20916   46087
70578   37746
31396   85745
38677   76047
51586   80370
33206   98673
40909   76255
86670   80370
71335   29711
90443   51586
76017   23086
64608   80370
46749   24742
89544   43543
41857   46279
42787   58205
73907   67100
62371   14872
24918   98011
51056   79598
39721   34796
67175   25915
30403   36271
64135   11780
76994   78902
66535   15092
59032   94333
75831   31184
30096   11447
23350   36783
59712   31994
38953   28778
60226   50228
82255   72338
36348   68865
76999   31396
10164   31710
15946   18029
77511   30248
95601   35450
18152   49627
32771   25915
20404   31396
61545   46279
34285   87463
84576   40124
51878   51586
88769   21515
63200   81326
68855   28497
65595   53032
48751   33285
60205   88896
96460   11367
89979   80045
11820   22373
83877   11780
20276   40124
19438   81902
94604   22373
14247   67536
89516   18681
44165   80045
58766   24742
11456   26306
11021   89613
55218   59490
74173   22743
46876   80459
63558   31935
64004   24611
72949   68564
57103   62092
95565   68564
16875   38769
81532   62587
15150   22210
74559   88896
62813   61861
29326   13612
81512   68564
49315   98827
76486   25915
42556   26135
72818   52964
24550   43656
64689   70406
73254   19265
93699   68564
53060   87046
93009   81902
39670   67615
61036   67631
45671   40413
41312   80045
49132   81902
38018   91922
71072   75073
22869   27664
55057   27814
24941   27959
84686   71679
28947   74369
25665   57496
78778   23305
14626   64462
37342   43855
59900   22416
43285   98392
92065   90613
20557   68564
45377   56858
14449   55097
97504   57790
53508   80370
39463   40124
40767   68564
64115   84078
57015   38612
10790   11780
39059   48255
97687   23054
80185   40124
42697   21344
84512   30568
88890   60974
26625   25773
23057   60654
86691   40392
19977   27723
20885   35230
82396   92827
95747   20497
70767   19369
36646   58544
55189   97285
88283   66161
61823   88896
81975   98911
96120   58310
27584   13612
29777   93381
83851   81326
68499   14896
71570   80045
83910   33934
72510   19369
29704   53243
58042   94333
10666   66744
25477   38332
46516   71338
11780   81760
60016   44454
76061   88896
45171   42137
16022   31396
43064   80370
74174   94333
75767   10987
94834   41861
43884   25498
73079   82486
49817   93178
84945   88121
37442   68004
75204   52912
88344   57580
78701   55148
79748   40124
74272   34796
32505   73879
74004   40075
97970   88796
43969   81902
34338   27951
56706   51586
70683   13612
51351   41678
15913   56236
34587   11780
27138   92114
81477   85239
37366   34453
15828   68865
29715   56858
97538   80370
16406   55594
68956   18077
21846   88896
76758   36425
59057   25915
43840   82650
67201   41066
49427   70257
41187   14872
36754   24495
23374   47449
39822   68865
66021   70536
42652   43243
24842   88896
24280   24742
88867   28631
89241   86694
23591   62627
59260   48813
50605   28489
24330   84536
25882   80024
35776   62926
54141   50228
75680   40124
84399   31530
78265   80370
87750   13922
36091   75968
27814   53359
63430   34796
63140   85215
81319   68564
89693   56300
44939   86165
78937   88896
34287   57052
60288   22373
39738   97201
66981   15143
93466   85978
43980   23335
50378   24498
65798   80045
33048   70536
74858   51594
41614   26882
78108   87082
95851   39538
55294   27347
91809   51930
18352   94333
92466   41921
20367   84778
94765   21872
70536   59326
83561   73432
80370   31935
70474   44396
96303   44391
12398   89041
23108   25947
53083   21157
99161   24742
85566   15007
32257   68564
46065   50230
63630   14872
42636   97201
94467   24904
62773   20111
56672   21157
25886   30403
13184   92058
24742   94333
69268   31396
22434   77346
12984   76178
27117   43656
10754   57124
24873   75979
39306   25915
68234   84487
17427   40124
97952   20994
33373   94333
76327   14493
45608   30947
48367   22373
54606   71965
24726   25915
10736   35060
13367   53242
95178   56815
27296   56858
68391   64705
98563   38903
20841   80370
20931   11515
60534   73652
44041   90593
39264   69166
12510   77382
65091   14872
73605   78383
43630   50005
80045   78823
17857   66318
71065   13612
67686   73652
40016   11780
96408   29692
34507   81902
10576   22373
62967   92940
68474   80370
67663   49384
27217   70536
45444   94221
16316   80370
53563   68564
76310   56858
56858   69426
96287   30104
80543   29117
82061   84323
44833   20029
58023   41150
93209   56858
19697   60022
53393   23230
97156   56858
13069   63002
72142   31122
57137   49844
48483   38592
72970   69357
93043   25915
56792   15463
73491   80370
95205   30947
84502   92854
50655   31935
81326   86245
30947   21547
81476   73108
54995   86542
88684   80659
16695   77477
67522   17661
14444   24717
48169   93182
77304   62773
10022   22838
85352   68865
88896   34807
80571   21157
75090   87473
45429   57148
38945   91244
70349   21157
13113   56858
34796   40124
32195   49176
28292   57181
14969   84572"""


list_inputs = input.split()

list1 = []
list2 = []
i=0

while i < len(list_inputs):
    list1.append(list_inputs[i])
    list2.append(list_inputs[i+1])
    i += 2

list1.sort()
list2.sort()

distance = 0

for i in range(len(list1)):
    distance += abs(int(list1[i]) - int(list2[i]))

print(distance)



