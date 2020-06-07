@objects
   header-nav                   xpath         //*[@id="mainNav"]
   header-subnav                xpath         //*[@id="universalCartTimerBannerId"]
   header-ismheader             xpath         //*[@id="vvNamIsm"]
   header-eventcontentbox 		xpath         /html/body/div[2]/div/div[2]
   header-eventinfoheader 		xpath         /html/body/div[2]/div/div[1]
   header-logo            		xpath         //*[@id="mainNav"]/div/div/div[1]/div[1]/div/div/a
   header-Myevent         		xpath         //nav[@id='block-iom-main-navigation-block']//a[contains(text(),'My Events')]
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
   header-eventinfodec    xpath         /html/body/div[2]/div/div[2]/div[1]/div/div[2]
   header-eventlimithead  		xpath         /html/body/div[2]/div/div[2]/div[2]/div[1]
   header-eventlimitdec   		xpath         /html/body/div[2]/div/div[2]/div[2]/div[2]
   header-eventlimitselec 		xpath         /html/body/div[2]/div/div[2]/div[3]/div[1]
   header-eventlimitselecdec 	xpath         /html/body/div[2]/div/div[2]/div[3]/div[2]
   header-eventlimitpromohead 	xpath         /html/body/div[2]/div/div[2]/div[4]/div[1]
   header-eventlimitpromodec 	xpath         /html/body/div[2]/div/div[2]/div[4]/div[2]
   
   
= Header =
   @on *   
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
   
   header-eventdate:
        on top left edge header-eventinfoheader 32px right, 47px bottom
        below header-logo 84px
        below header-infoicon 48px
        text is "Tue, Dec 15, 2020 @ 08:00 pm"
        inside screen 135px top
        visible
        width ~193px
        inside header-eventinfoheader 47px top, 32px left, ~415px right , 18px bottom
        height 21px
        css font-weight contains "400"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "14px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "left"
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
        
        
   header-eventplace:
        on top right edge header-eventinfoheader ~367px left, 47px bottom
        below header-logo 84px
        below header-infoicon 48px
        text is "UCF GA RESERVED VENUE"
        inside screen 135px top
        visible
        width 176px
        inside header-eventinfoheader 47px top, ~273px left, 192px right , 18px bottom
        height 21px
        css font-weight contains "400"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "14px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "left"
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
 
= Event Info Container =
   @on *   
   header-eventinfotext:
        on top left edge header-eventinfoheader 32px right, 104px bottom
        below header-logo 141px
        below header-infoicon 105px
        above header-eventinfodec 6px
        text is "Event Information"
        inside screen 192px top
        visible
        width 402px
        inside header-eventcontentbox 18px top, 32px left, 206px right , 324px bottom
        height 30px
        css font-weight contains "600"
        css color contains "rgba(38, 38, 38, 1)"
        css font-size contains "20px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "30px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
   header-eventinfodec:
        on top left edge header-eventinfoheader 32px right, 140px bottom
        below header-logo 177px
        below header-infoicon 141px
        below header-eventinfotext 6px
        text is "Review the below information related to any ticket limits and/or offers set for this event."
        inside screen 228px top
        visible
        width 402px
        inside header-eventcontentbox 54px top, 32px left, 206px right , 270px bottom
        height 48px
        css font-weight contains "400"
        css color contains "rgba(38, 38, 38, 0.65)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "24px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
   header-eventlimithead:
        on top left edge header-eventinfoheader 32px right, 206px bottom
        below header-logo 243px
        below header-infoicon 207px
        below header-eventinfotext 72px
        text is "Event Limit"
        inside screen 294px top
        visible
        width 576px
        inside header-eventcontentbox 120px top, 32px left, 32px right , 228px bottom
        height 24px
        css font-weight contains "600"
        css color contains "rgba(38, 38, 38, 1)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "24px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
        
   header-eventlimitdec:
        on top left edge header-eventinfoheader 32px right, 230px bottom
        below header-logo 267px
        below header-infoicon 231px
        below header-eventinfotext 96px
        text is "This event has a minimum ticket limit of 1 and a maximum ticket limit of 999 per account."
        inside screen 318px top
        visible
        width 576px
        inside header-eventcontentbox 144px top, 32px left, 32px right , 180px bottom
        height 48px
        css font-weight contains "400"
        css color contains "rgba(38, 38, 38, 0.65)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "24px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
        
   header-eventlimitselec:
        on top left edge header-eventinfoheader 32px right, 296px bottom
        below header-logo 333px
        below header-infoicon 297px
        below header-eventinfotext 162px
        text is "Selecting Seats"
        inside screen 384px top
        visible
        width 576px
        inside header-eventcontentbox 210px top, 32px left, 32px right , 138px bottom
        height 24px
        css font-weight contains "600"
        css color contains "rgba(38, 38, 38, 1)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "24px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
        
   header-eventlimitselecdec:
        height ~48px
        on top left edge header-eventinfoheader 32px right, 320px bottom
        below header-logo 357px
        below header-infoicon 321px
        below header-eventinfotext 186px
        text is "Based on the seats you select, there may be specific ticket limits enforced which will be indicated after selection."
        inside screen 408px top
        visible
        width 576px
        inside header-eventcontentbox 234px top, 32px left, 32px right , 90px bottom
        height 48px
        css font-weight contains "400"
        css color contains "rgba(38, 38, 38, 0.65)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "24px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
        
   header-eventlimitpromohead:
        on top left edge header-eventinfoheader 32px right, ~386px bottom
        below header-logo ~423px
        below header-infoicon 387px
        below header-eventinfotext 252px
        text is "Promo Codes"
        inside screen 474px top
        visible
        width 576px
        inside header-eventcontentbox 300px top, 32px left, 32px right , 48px bottom
        height 24px
        css font-weight contains "600"
        css color contains "rgba(38, 38, 38, 1)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "24px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
        
   header-eventlimitpromodec:
        on top left edge header-eventinfoheader 32px right, 410px bottom
        below header-logo 447px
        below header-infoicon 411px
        below header-eventinfotext 276px
        text is "This event has available promo codes. Take advantage of the offer by entering the promo code."
        inside screen 498px top
        visible
        width 576px
        inside header-eventcontentbox 324px top, 32px left, 32px right , 0px bottom
        height 48px
        css font-weight contains "400"
        css color contains "rgba(38, 38, 38, 0.65)"
        css font-size contains "16px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "start"
        css font-stretch contains "100%"
        css line-height is "24px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
= Event Info Footer =
   @on *            
   header-gotit:
        on top left edge header-eventinfoheader 545px right, 482px bottom
        below header-logo 519px
        below header-infoicon 483px
        text is "Got it"
        inside screen 570px top
        visible
        width 62px
        inside header-gotitbottom 24px top, 545px left, 33px right , 32px bottom
        height 36px
        css font-weight contains "600"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "14px"
        css font-family contains "Averta"
        css outline-width contains "0px"
        css text-align contains "center"
        css font-stretch contains "100%"
        css line-height is "34.02px"
        css border-bottom-left-radius contains "2px"
        css border-bottom-right-radius contains "2px"
        css border-top-right-radius contains "2px"
        css border-top-left-radius contains "2px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "12px"
        css padding-right contains "12px"
        css padding-top contains "0px"