from ytmusicapi import YTMusic
from pprint import pprint
from module_globalVar import globalVar

def getYtbMusicUrl(args):
    ytmusic = YTMusic()
    result = ytmusic.search(query = args[0])
    resultReMap = tuple(
        map(
            lambda x:
                ("[%s]" %x.get('resultType', 'unknownType'), 
                x.get('title', 'unknownTitle'), 
                "+".join(tuple(map(lambda y:y.get('name','unknownArtist'), x.get('artists', {})))), 
                x.get('album', {}).get('name', 'unknownName')),
            result
            )
        )
    # pprint(result)
    # pprint(resultReMap)
    vidArr = tuple(map(lambda z:z.get('videoId'), result))
    resultReMapFiltered = []
    vidArrFiltered = []
    for ind_i, vid_i in enumerate(vidArr):
        if vid_i:
            # resultReMapFiltered.append("|".join(resultReMap[ind_i]))
            resultReMapFiltered.append("    ".join(resultReMap[ind_i]))
            vidArrFiltered.append(vid_i)
    globalVar.set_value("vidArr", vidArrFiltered)
    # headerShow = "|Type|Title|Artist|Album|\n|:----:|:----:|:----:|:----:|"
    # resultShow = "|"+"|\n|".join(resultReMapFiltered)+"|"
    # return "已为您找到以下结果\n%s" %str(resultShow).replace("|", "\|").replace("-", "\-").replace("(", "\(").replace(")", "\)")
    headerShow = "Type    Title    Artist    Album\n"
    resultShow = "\n".join(resultReMapFiltered)
    return "已为您找到以下结果\n%s" %str(resultShow)