import rollingAvg
import math

print "Testing rollingAvg()"
tmpList = [494487, 482089, 464788, 461570, 467335, 458157, 449892, 448518, 452387, 451837, 441890, 430802, 450211, 466005, 435834, 383871, 388919, 399417, 385217, 388899, 390789, 384132, 381428, 380610, 383290, 385421, 382180, 376287, 374738, 374690]

tmpList = [7558, 7463, 7428, 7343, 7194, 7208, 7092, 7041, 7008, 6899, 6839, 6771, 6743, 6674, 6583, 6540, 6435, 6333, 4295, 4261, 4236, 4207, 4162, 4099, 4088, 4142, 4105, 4101, 4104, 4040]

print len(tmpList)
result = rollingAvg.rollingAvg(tmpList, 2)
i = 0
while i < len(tmpList) :
    x = math.fabs(result[i][0] - tmpList[i])/result[i][1]
    print "%03d" % i \
	+ ": %6d" % tmpList[i] \
	+ "; m: %9.2f" % result[i][0] \
	+ "; s: %9.2f" % result[i][1] \
	+ "; s(%): " + "%1.4f" % x
    i += 1
