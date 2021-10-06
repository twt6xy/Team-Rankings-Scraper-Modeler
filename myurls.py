#!/usr/bin/env python
# coding: utf-8

# In[ ]:


urls2020 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games"
    ]

urls2019 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2020-03-12",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2020-03-12"
]

urls2018 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2019-04-09",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2019-04-09"
]

urls2017 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2018-04-03",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2018-04-03"
    ]

urls2016 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2017-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2017-04-04"
    ]

urls2015 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2016-04-05",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2016-04-05"
    ]

urls2014 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2015-04-06",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2015-04-06"
    ]

urls2013 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2014-04-07",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2014-04-07"
    ]

urls2012 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2013-04-08",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2013-04-08"
    ]

urls2011 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2012-04-02",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2012-04-02"
    ]

urls2010 = [
    "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/offensive-rebounds-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/shooting-pct?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-2-pointers?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/points-from-3-pointers?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/defensive-rebounds-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/turnovers-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-shooting-pct?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-offensive-rebounds-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-defensive-rebounds-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-blocks-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-steals-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-assists-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/opponent-turnovers-per-game?date=2011-04-04",
    "https://www.teamrankings.com/ncaa-basketball/stat/win-pct-all-games?date=2011-04-04"
    ]

