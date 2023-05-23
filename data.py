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
                 },
                 
                 "https://www.speedtest.net":
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
                },

                "https://wwww.foxnews.com":
                {"specifics":"ablock=true;",
                 "main-menu-link":'css selector;a.logo[href="https://www.foxnews.com"]',
                 "endpoints":
                 {
                     "Login-page": 'partial link text;Log In', #direct link does not work.
                     "Politics": 'css selector;a[href="https://www.foxnews.com/politics"]',
                     "World": 'css selector;a[href="https://www.foxnews.com/world"]',
                 },
                #sub-endpoints unavailable
                },

                "https://www.aol.com":
                {"specifics":"ablock=true;",
                 "main-menu": 'css selector;a.logo-link',
                 "endpoints":
                 {
                     # website mostly uses xpath. Not ideal for this project
                 },
                  
                },
                "https://www.sharepoint.com":
                {"specifics":"ablock=true;",
                 "main-menu": 'css selector;a#uhfLogo',
                 "endpoints":
                 {
                     "Login-page": 'css selector;div#mectrl_headerPicture',
                     "Teams": 'css selector;a#l0_Teams.c-uhf-nav-link',
                     "Windows":'partial link text;Windows',
                 },
                  "sub-endpoints":{
                      "Teams": {"See plans and pricing": 'class name;link-group',
                                },
                       "Windows": {"Get windows11": 'css selector;a.c-call-to-action',         
                  },
                }
                },

                "https://www.airbnb.ca":
                {"specifics":"ablock=true;",
                 "main-menu-link":"css selector;button[aria-label='Close']", #opening this webpage always shows a pop up.
                 "endpoints":
                 {
                     "Privacy": 'partial link text;Privacy',
                     "Terms": 'partial link text;Terms',
                     "Sitemap": 'partial link text;Sitemap',
                 },

                 "sub-endpoints":{
                     "Airbnb Privacy": {
                        "Privacy Policy": 'partial link text;Privacy Policy for the United States',
                        "Privacy Policy": 'partial link text;Privacy Policy for Outside the U.S. (English)',
                        "Privacy Policy": 'partial link text;Privacy Policy for Outside the U.S. (French)',
                        "Privacy Policy": 'partial link text;Cookie Policy',
                     },
                     "Terms of Service": {
                        "Schedule": 'partial link text;Schedule 1',
                        "Payment Terms of Service": 'partial link text;Payments Terms of Service',
                        "Hosting": 'partial link text;5. Hosting on Airbnb.',

                     },
                 }
                 },

                 "https://www.bestbuy.com":
                {"specifics":"ablock=true;",
                 "main-menu-link": ["css selector;img[src='https://www.bestbuy.com/~assets/bby/_intl/landing_page/images/maps/canada.svg']", 'css selector;.logo_3ePCc'],
                #Need to press Location before going into the site.
                 "endpoints":
                 {
                     "Account": 'partial link text;Account',
                     "Stores": 'partial link text;Stores',
                     "Cart": 'partial link text;Cart',
                 },

                 "sub-endpoints":{
                     "Account": {
                        "Sign in": 'css selector;svg._13Pgk.create-account-link-chevron._2kWmn',
                        "Password show text": 'partial link text:Show',
                     },
                     "Stores":{
                         "Browsing location": 'partial link text;browse all locations.',
                     },
                     "Cart": {
                         "quick and easy": 'partial link text;Quick and Easy Store Pickup',
                         "Freeshipping": 'partial link text;Free shipping over $35',
                         "Low Price": 'partial link text;Low Price Guarantee',
                     },
                 }
                 },

                }
