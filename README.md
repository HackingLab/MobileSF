# Mobile-Security-Framework (HackingLab 定制版 MobSF)
Version: v0.9.2 beta
* 官方地址: https://github.com/ajinabraham/Mobile-Security-Framework-MobSF 
* HackingLab定制版地址: https://github.com/HackingLab/MobileSF （官方更新了，但还是有Bug，不过很值得尝试，欢迎大牛批评指正。）
##功能介简介:
* 1.支持安卓APK静态分析,动态分析
(动态分析可使用MobileSafeFramework官方提供的VirtualBox虚拟机也可以使用用户自己的手机进行测试,需要开启USB调试并安装响应的测试软件)
* 2.支持IOS应用静态分析(需要使用MacOS)
##功能介绍[官方]:
* MobSF是一款智能的,集多种功能于一体的移动App(安卓/IOS)测试工具框架.他支持安卓/IOS应用和ZIP格式的源码包
* 静态分析: 静态分析可以查看源代码,检测不安全的权限/配置,检测代码中不安全的ssl管理(如重写,绕过等),弱的加密算法,代码混淆,导入权限,硬编码密钥,不恰当的危险的API使用,敏感信息泄露,不安全的文件存储等.
* 动态分析: 动态分析是在虚拟机中/或配置好的设备中运行APP并进行安全检测.对应用进行更深层的检测,包括网络抓包,解密HTTPS流量,应用dump,日志,错误,崩溃,调试信息,调用栈,应用资源,属性,数据库等.在这个框架中,你也可以自行定制自己的测试规则.最后会生成一份快速简洁的测试报告.以后我们也会拓展该框架,使得其能够支持其他的移动平台,如Tizen,WindowsPhone等.
##界面截图: 
系统首页界面
[![index](http://mobilesf.hackinglab.cn/media/14676328520038/14676334645872.jpg)
进行静态分析
[![index](http://mobilesf.hackinglab.cn/media/14676328520038/14676330860451.jpg)
apk动态分析过程会自动测试多个安全项目,并自动进行屏幕截图.
不仅包括Activities相关测试,还能够自动对网络流量进行分析,并保存由APP发出的HTTP/HTTPS请求.

#HackingLab XsecLab Team 
* 汉化并改进提示
* 优化部分性能问题
* http://www.xseclab.com/
* http://hackinglab.cn/

#
<p align="center">
  <img src="https://cloud.githubusercontent.com/assets/4301109/14958530/d5fb36ac-10a8-11e6-93b9-8859fd0158b6.png">
</p>

Mobile Security Framework (MobSF) is an intelligent, all-in-one open source mobile application (Android/iOS) automated pen-testing framework capable of performing static and dynamic analysis. It can be used for effective and fast security analysis of Android and iOS Applications and supports both binaries (APK &amp; IPA) and zipped source code. MobSF can also perform Web API Security testing with it's API Fuzzer that can do Information Gathering, analyze Security Headers, identify Mobile API specific vulnerabilities like XXE, SSRF, Path Traversal, IDOR, and other logical issues related to Session and API Rate Limiting.

[![support](https://baikal.io/badges/ajinabraham/mobsf)](https://baikal.io/ajinabraham/mobsf) [![License](https://img.shields.io/:license-gpl3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/ajinabraham/Mobile-Security-Framework-MobSF/)
[![python](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/d49e36d69236411bb854214737f6dfa1/badge.svg)](https://www.quantifiedcode.com/app/project/d49e36d69236411bb854214737f6dfa1)

## Documentation
* https://github.com/ajinabraham/Mobile-Security-Framework-MobSF/wiki/1.-Documentation

## Presentation Slides
* [NULLCON 2016](https://www.slideshare.net/ajin25/nullcon-goa-2016-automated-mobile-application-security-testing-with-mobile-security-framework-mobsf)
* [c0c0n 2015](https://www.slideshare.net/ajin25/automated-security-analysis-of-android-ios-applications-with-mobile-security-framework-c0c0n-2015)

## Video Course
* Automated Mobile Application Security Assessment with MobSF: https://opsecx.com/index.php/product/automated-mobile-application-security-assessment-with-mobsf/

## What's New?
* See Changelog: https://github.com/ajinabraham/Mobile-Security-Framework-MobSF/wiki/3.-Changelog

## Queries

* Features Requests: [@ajinabraham](https://twitter.com/ajinabraham) or [@OpenSecurity_IN](https://twitter.com/OpenSecurity_IN). 
* Open Bugs Here:  https://github.com/ajinabraham/Mobile-Security-Framework-MobSF/issues
* Please add the log files `logs/MobSF.log` and `logs/webproxy.log` while opening bugs.

## Screenshots

###Static Analysis - Android APK 

![android-static-analysis-apk](https://cloud.githubusercontent.com/assets/4301109/13614857/7a39189c-e598-11e5-90ff-6357b6c320bd.png)
![android-static-analysis-apk2](https://cloud.githubusercontent.com/assets/4301109/13614896/b7b7b53e-e598-11e5-84b5-e69c56c230a3.png)

###Static Analysis - iOS IPA

![ios-static-analysis-ipa](https://cloud.githubusercontent.com/assets/4301109/13614950/e8174ac8-e598-11e5-8e03-d40ad7d9e5a4.png)

###Dynamic Analysis - Android APK

![android-dynamic-analysis](https://cloud.githubusercontent.com/assets/4301109/13615043/6fe62028-e599-11e5-9c50-e44adbba114a.png)
![android-dynamic-report](https://cloud.githubusercontent.com/assets/4301109/13615800/104cc424-e59d-11e5-9a98-2e3b2aff7222.png)
![android-dynamic-report2](https://cloud.githubusercontent.com/assets/4301109/13615767/f04e5c1e-e59c-11e5-9ad1-b31598024ad4.png)
![android-dynamic-expact](https://cloud.githubusercontent.com/assets/4301109/13615882/6f4d9f16-e59d-11e5-9ec9-3b4c47e37389.png)

###Web API Fuzzer

![api-fuzzer-start-scan](https://cloud.githubusercontent.com/assets/4301109/13615144/e992ecda-e599-11e5-88d5-e7c310980b62.png)
![api-fuzzer-start-report](https://cloud.githubusercontent.com/assets/4301109/13615236/5d8df210-e59a-11e5-827a-ccf642e96609.png)

##Credits

* Bharadwaj Machiraju (@tunnelshade_) - For writing pyWebProxy from scratch
* MindMac - For writing Android Blue Pill
* Thomas Abraham - For JS Hacks on UI.
* Anto Joseph (@antojosep007) - For the help with SuperSU.
* Tim Brown (@timb_machine) - For the iOS Binary Analysis Ruleset.
* Abhinav Sejpal (@Abhinav_Sejpal) - For poking me with bugs and feature requests.
* Anant Srivastava (@anantshri) - For Activity Tester Idea
* Amrutha VC (@amruthavc) - For the new MobSF logo

