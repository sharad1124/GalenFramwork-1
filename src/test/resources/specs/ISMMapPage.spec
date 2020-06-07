@objects
   header-nav             xpath         //*[@id="mainNav"]
   header-subnav          xpath         //*[@id="universalCartTimerBannerId"]
   header-ismheader       xpath         //*[@id="vvNamIsm"]
   header-eventcontentbox xpath         /html/body/div[2]/div/div[2]
   header-eventinfoheader xpath         /html/body/div[2]/div/div[1]
   header-logo            xpath         //*[@id="mainNav"]/div/div/div[1]/div[1]/div/div/a
   header-Myevent         xpath         //nav[@id='block-iom-main-navigation-block']//a[contains(text(),'My Events')]
   header-signin          xpath         //*[@id="invoke-signin-modal"]
   header-language        xpath         //*[@id="edit-item"]/div/div[1]
   header-cart            xpath         //*[@id="universalCartIconSVGId"]
   header-infoicon        xpath         //*[@id="universalCartTimerBannerId"]/div/div/div/div[1]/div
   header-infotext        xpath         //*[@id="universalCartTimerBannerId"]/div/div/div/div[1]/span
   header-checkinfoevent  xpath         //*[@id="universalCartTimerBannerId"]/div/div/div/div[3]
   header-imagefoevent    xpath         //*[@id="universalCartTimerBannerId"]/div/div/div/div[3]/svg
   header-qty             xpath         //*[@id="qtyLabel"]
   header-event           xpath         /html/body/div[2]/div/div[1]/div/div[1]
   header-eventdate       xpath         /html/body/div[2]/div/div[1]/div/div[2]/span[1]
   header-eventplace      xpath         /html/body/div[2]/div/div[1]/div/div[2]/span[2]
   header-gotit           xpath         /html/body/div[2]/div/div[3]/button
   header-gotitbottom     xpath         /html/body/div[2]/div/div[3]
   header-eventinfotext   xpath         /html/body/div[2]/div/div[2]/div[1]/div/div[1]
   
      
= Header =
   @on *
   header-logo:
        inside screen 3px top
        inside screen 68px left
        visible
        width 64px
        aligned horizontally all header-signin 4px
        aligned horizontally all header-language 24px
        aligned horizontally all header-cart 30px
        aligned vertically left header-infoicon 46px
        inside header-nav 3px top, 68px left, 3px bottom, 1548px right
        aligned horizontally centered header-nav 22px
        left-of header-signin 1273px
        left-of header-language 1374px
        left-of header-cart 1451px
        height 48px
        css font-weight contains "300"
        css color contains "rgba(0, 44, 95, 1)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "21px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
= Sign IN =
   @on *    
   header-signin:
        inside screen 0px top
        visible
        text is "Sign In"
        width 79px
        aligned horizontally all header-logo 24px
        aligned horizontally all header-language 24px
        aligned horizontally all header-cart 63px
        inside header-nav 0px top, 1405px left, 4px bottom, 196px right
        aligned horizontally centered header-nav 22px
        left-of header-language 22px
        left-of header-cart 99px
        height 50px
        css font-weight contains "300"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "50px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "29px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
= Language =
   @on *        
   header-language:
        inside screen 0px top
        visible
        text is "EN"
        width 52px
        aligned horizontally all header-signin 24px
        aligned horizontally all header-logo 24px
        aligned horizontally all header-cart 63px
        inside header-nav 0px top, 1506px left, 0px bottom, 122px right
        aligned horizontally centered header-nav 22px
        right-of header-signin 22px
        right-of header-logo 1374px
        left-of header-cart 25px
        height 54px
        css font-weight contains "300"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "54px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
   header-cart:
        inside screen 15px top
        visible
        width ~24px
        aligned horizontally all header-signin 26px
        aligned horizontally all header-language 30px
        aligned horizontally all header-cart 63px
        inside header-nav 15px top, 1583px left, 15px bottom, 73px right
        aligned horizontally centered header-subnav 47px
        right-of header-signin 99px
        right-of header-language 25px
        right-of header-logo 1451px
        height 24px
        css font-weight contains "300"
        css color contains "rgba(38, 38, 38, 1)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "21px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
= Sub Header =
   @on *        
   header-infoicon:
        inside screen 63px top
        visible
        width 22px
        inside header-subnav 9px top, 68px left, 1590px right , 4px bottom
        height 27px
        css font-weight contains "300"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "14px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "21px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
        
   header-infotext:
        text is "You may have access to additional tickets and special events once you sign in"
        inside screen 63px top
        visible
        width 499px
        inside header-subnav 9px top, 98px left, 1083px right , 10px bottom
        aligned horizontally centered header-subnav 363px
        left-of header-signin 808px
        left-of header-language 909px
        left-of header-cart 986px
        height 21px
        css font-weight contains "400"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "14px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "21px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
   header-checkinfoevent:
        contains header-checkinfoevent
        text is "Check Event Info"
        inside screen 62px top
        visible
        width 130px
        inside header-subnav 8px top, 629px left, 921px right , 8px bottom
        height 24px
        css font-weight contains "300"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "14px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "21px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
   header-qty:
        contains header-qty
        on top left edge header-logo 0px left, 103px bottom
        below header-logo 55px
        below header-infoicon 16px
        text is "Qty"
        inside screen 106px top
        visible
        width 35px
        inside header-ismheader 12px top, 68px left, 1577px right , 12px bottom
        height 36px
        css font-weight contains "300"
        css color contains "rgba(51, 51, 51, 1)"
        css font-size contains "20px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "36px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"