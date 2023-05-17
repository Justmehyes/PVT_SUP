WEBSITE_LIST = {"https://www.youtube.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "login-page":   'direct-link;signin',
                  "video":  'css selector;ytd-rich-item-renderer'
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{"trending":'relies_prev:partial link text;Trending',
                                   "music":   'relies_prev:partial link text;Music',
                                   "gaming":  'relies_prev:partial link text;Gaming',
                                   "news":    'relies_prev:partial link text;News',
                                   "sports":  'relies_prev:partial link text;Sports',
                                   "learning":'relies_prev:partial link text;Learning'
                                   },
                      "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                  },
                      "music":{"video":'rand_ind:css selector;ytd-video-renderer'
                               },
                      "gaming":{"video":"rand_ind:css selector;ytd-video-renderer"
                          
                      },
                  }
                 }
                }

WEBSITE_LIST = {"https://www.speedtest.net":
                {"specifics":"ablock=true;",
                 "main-menu-link":'refresh_sens:id;consent_blackbar',
                 "endpoints":
                 {
                    "Login-page": 'direct-link;login', 
                    "Apps": 'partial link text;Apps',
                    "About": 'partial link text;About',
                    "Analysis": 'partial link text;Analysis',
                 },
                 "sub-endpoints":{
                     "Apps": {"Speedtest for IOS": 'partial link text;Speedtest for iOS',
                              "Speedtest for Android": 'partial link text;Speedtest for Android',
                              "Speedtest for Windows": 'partial link text;Speedtest for Windows',
                              },
                     "About": {"iOS": 'partial link text;iOS',
                               "Android": 'partial link text;Android',
                               "macOS": 'partial link text;macOS',
                     },
                 }   
                } 
                }

WEBSITE_LIST = {"https://wwww.foxnews.com":
                {"specifics":"ablock=true;",
                 "main-menu-link":'css selector;a.logo[href="https://www.foxnews.com"]',
                 "endpoints":
                 {
                     "Login-page": 'partial link text;Log In', #direct link does not work.
                     "Politics": 'css selector;a[href="https://www.foxnews.com/politics"]',
                     "World": 'css selector;a[href="https://www.foxnews.com/world"]',
                 },
                #sub-endpoints unavailable
                }
                }

WEBSITE_LIST = {"https://www.aol.com":
                {"specifics":"ablock=true;",
                 "main-menu": 'css selector;a.logo-link',
                 "endpoints":
                 {
                     #
                 },
                  
                }

}



