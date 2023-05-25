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

                 "https://www.skype.com":
                 {"specifics":"ablock=true;",
                  "main-menu-link":'partial link text;Skype',
                  "endpoints":
                  {
                      "Downloads": 'partial link text;Downloads',
                      "Skype to Phone": 'partial link text;Skype to Phone',
                      "Skype Number": 'partial link text;Skype Number',
                  },
                  
                  "sub-endpoints":{
                      "Downloads":{
                          "Skype Download": 'partial link text;Get Skype for Windows 10 & 11',
                          "Open Skype": 'partial link text;Skype Insider Program',
                          "Mobile Device": 'partial link text;Mobile',
                     },
                      "Skype to Phone": {
                          "United states": 'partial link text;Continue',
                          "India": "css selector;button.IzjkL._2Y_WL.FiOTW[data-bi-id='buyNow-in-mixed-800-ft-variantD-showByNowBtn-false']",
                          "N.A": 'partial link text;Try free for a month',
                     },
                     "Skype Number":{
                         "U.K": 'partial link text;United Kingdom',
                         "Germany": 'partial link text;Germany',
                         "HongKong SAR": 'partial link text;Hong Kong SAR',
                     },
                      },
                     
                 },

                 "https://wwww.flickr.com":
                 {"specifics":"ablock=true;",
                  "main-menu": 'css selector;a.main-logo.new-logo',
                  "endpoints":
                  {
                      "login": 'partial link text;Log In',
                      "About page": 'partial link text;About',
                      "Jobs": 'partial link text;Jobs',
                  },
                  "sub-endpoints":{
                    "About": {
                    "FlickrBlog": 'partial link text;Flickr blog',
                    "Guidelines": 'partial link text;Community guidelines',
                    "FAQ": 'partial link text;Visit our FAQ', 
                  },
                    "Jobs": {
                      "Openings": 'partial link text;View openings',
                      "Upload": 'partial link text;Upload',
                      "Login button": 'partial link text;Log In', 
                    }
                  },
                 },

                "https://wwww.gamefaqs.com":
                 {"specifics":"ablock=true;",
                  "main-menu":'partial link text;GameFAQs',
                  "endpoints":
                  {
                      "login": 'css selector;a[href="/user/login"]',
                      "Boards": 'partial link text;Boards',
                      "News": 'partial link text;News',
                  },
                  "sub-endpoints": {
                      "Boards": {
                          "GmaeBoards": 'partial link text;Game Boards',
                          "Community Boards": 'partial link text;Community Boards',
                          "More boards": 'partial link text;Special Interest Boards',
                      },
                      "News": {
                          "Releaases": 'partial link text;More Upcoming Releases >>',
                          "More Releases": 'partial link text;More New Releases >>',
                          "Contribution": 'partial link text; More New Contributions >>',
                      },
                  },
                },

                "https://www.sourceforge.net":
                {"specifics":"ablock=true;",
                 "main-menu":"css selector;img.sf-logo-full",
                 "endpoints":
                 {
                     "login": 'partial link text;Login',
                     "Join": 'partial link text;Join & Create',
                     "Browse": 'partial link text;Browse Business Software',
                     "Open Software": 'partial link text;Browse Open Source Software',
                 },
                 "sub-endpoints": {
                     "Join": {
                        "Create": 'partial link text;Create Your Project Now',
                        "Apache": 'partial link text;Apache OpenOffice',
                        "PortableApps": 'partial link text;PortableApps',
                     },
                     "Browse":{
                         "website": 'partial link text;monday.com',
                         "website": 'partial link text;Miro',
                         "website": 'partial link text;Acronis Cyber Protect',
                     },
                     "Open Software": {
                         "Software": "partial link text;Microsoft's TrueType core fonts",
                         "Software": 'partial link text;SAP NetWeaver Server Adapter for Eclipse',
                         "Software": 'partial link text;AutoClicker',
                     }
                 }
                
                },
                "https://www.telegram.org":
                {"specifics":"ablock=true;",
                 "main-menu": 'css selector;div.tl_main_logo.play',
                 "endpoints":
                 {
                     "telegram for android": 'css selector;a.tl_main_download_link.tl_main_download_link_android',
                     "telegram for Desktop": 'css selector;a.tl_main_download_desktop_link.tl_main_download_link_td',
                     "News": 'partial link text;Recent News',
                 },
                 "sub-endpoints":{
                     "News":{
                         "twitter": 'css selector;a[data-track="Follow/Twitter"]',
                         "TelegramNews": 'partial link text;Power Saving Mode and More',
                         "TelegramNews": 'partial link text;Shareble Chat Folders, Custom Wallpapers and More',
                     },
                     "Telegram for android":{
                         "Download": 'partial link text;Download Telegram',
                         "Steps to download": 'partial link text;this page',
                         "Updates": 'partial link text;telegram.org',
                     },
                     "Telegram for Desktop":{
                         "Windows": 'partial link text;Windows',
                         "Portable Version": 'partial link text;Portable version',
                         "Portable Version": 'partial link text;Show all platforms',
                     },
                 },
                },

                "https://www.researchgate.net":
                 {"specifics":"ablock=true;",
                  "main-menu": 'css selector;img[alt="ResearchGate"]',
                  "endpoints":
                  {
                      "Login": 'css selector;a.index-header__log-in',
                      "Join for free": 'partial link text;Join for free',
                      "Careers": 'partial link text;Careers',
                  },
                  "subendpoints":{
                    "Careers": {
                        "Security": 'partial link text;Security',
                        "Press": 'partial link text;Press',
                        "Imprint": 'partial link text;Imprint',
                    },
                    "Join for free":{

                    }, 
                  },  
                     
                 },
            }
              
