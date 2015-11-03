# HackingLab定制版Mobile Safe Framework
##Mobile Safe Framework Link
官方地址: https://github.com/ajinabraham/Mobile-Security-Framework-MobSF
HackingLab定制版地址: https://github.com/HackingLab/MobileSF
（Bug较多，小白暂时等一等，欢迎大牛批评。）
##功能介简介:
1.支持安卓APK静态分析,动态分析
(动态分析可使用MobileSafeFramework官方提供的VirtualBox虚拟机也可以使用用户自己的手机进行测试,需要开启USB调试并安装响应的测试软件)
2.支持IOS应用静态分析(需要使用MacOS)
##功能介绍[官方]:
MobSF是一款智能的,集多种功能于一体的移动App(安卓/IOS)测试工具框架.他支持安卓/IOS应用和ZIP格式的源码包

静态分析: 静态分析可以查看源代码,检测不安全的权限/配置,检测代码中不安全的ssl管理(如重写,绕过等),弱的加密算法,代码混淆,导入权限,硬编码密钥,不恰当的危险的API使用,敏感信息泄露,不安全的文件存储等.

动态分析: 动态分析是在虚拟机中/或配置好的设备中运行APP并进行安全检测.对应用进行更深层的检测,包括网络抓包,解密HTTPS流量,应用dump,日志,错误,崩溃,调试信息,调用栈,应用资源,属性,数据库等.在这个框架中,你也可以自行定制自己的测试规则.最后会生成一份快速简洁的测试报告.以后我们也会拓展该框架,使得其能够支持其他的移动平台,如Tizen,WindowsPhone等.
##界面截图: 
系统首页界面
![mobsfindex](http://mobilesf.hackinglab.cn/media/14465158168823/14465158298046.jpg)
进行静态分析
![](http://mobilesf.hackinglab.cn/media/14465158168823/14465159814524.jpg)
APK静态分析结果
![](http://mobilesf.hackinglab.cn/media/14465158168823/14465160058379.jpg)
进行动态分析,创建测试分析环境
![](http://mobilesf.hackinglab.cn/media/14465158168823/14465160513152.jpg)
开始进行分析
![](http://mobilesf.hackinglab.cn/media/14465158168823/14465162378420.jpg)
分析结果[官方]
![android-dynamic](https://cloud.githubusercontent.com/assets/4301109/9771195/1374d99a-5752-11e5-9b33-70ac6347164a.png)

apk动态分析过程会自动测试多个安全项目,并自动进行屏幕截图.
不仅包括Activities相关测试,还能够自动对网络流量进行分析,并保存由APP发出的HTTP/HTTPS请求.


# Mobile-Security-Framework
Version: v0.8.8beta
![mobsecfav](https://cloud.githubusercontent.com/assets/4301109/7418958/68ec3d44-ef8f-11e4-97e2-b26a3d723814.png)

Mobile Security Framework is an intelligent, all-in-one open source mobile application (Android/iOS) automated pen-testing framework capable of performing static and dynamic analysis. We've been depending on multiple tools to carry out reversing, decoding, debugging, code review, and pen-test and this process requires a lot of effort and time. Mobile Security Framework can be used for effective and fast security analysis of Android and iOS Applications. It supports binaries (APK & IPA) and zipped source code.

The static analyzer is able to perform automated code review, detect insecure permissions and configurations, and detect insecure code like ssl overriding, ssl bypass, weak crypto, obfuscated codes, improper permissions, hardcoded secrets, improper usage of dangerous APIs, leakage of sensitive/PII information, and insecure file storage. 
The dynamic analyzer runs the application in a VM or on a configured device and detects the issues at run time. Further analysis is done on the captured network packets, decrypted HTTPS traffic, application dumps, logs, error or crash reports, debug information, stack trace, and on the application assets like setting files, preferences, and databases. This framework is highly scalable that you can add your custom rules with ease. A quick and clean report can be generated at the end of the tests. We will be extending this framework to support other mobile platforms like Tizen, WindowsPhone etc. in future. 
###Static Analysis - Android APK 
![android-1](https://cloud.githubusercontent.com/assets/4301109/7418316/a200f318-ef8a-11e4-9828-8d696e386847.png)
![android-2](https://cloud.githubusercontent.com/assets/4301109/7418317/a28dac4a-ef8a-11e4-8716-09fa42532ee8.png)
###Static Analysis - iOS IPA
![ios](https://cloud.githubusercontent.com/assets/4301109/7418318/a29b1f88-ef8a-11e4-8d76-9883b7664501.png)

Sample Report: http://opensecurity.in/research/security-analysis-of-android-browsers.html

###Dynamic Analysis - Android APK
![android-dynamic](https://cloud.githubusercontent.com/assets/4301109/9771195/1374d99a-5752-11e5-9b33-70ac6347164a.png)

## Documentation
* https://github.com/ajinabraham/Mobile-Security-Framework-MobSF/wiki/Documentation

##Queries

* Features and Updates : [@ajinabraham](http://twitter.com/ajinabraham) or [@OpenSecurity_IN](http://twitter.com/OpenSecurity_IN). 
* Open Bugs Here - https://github.com/ajinabraham/YSO-Mobile-Security-Framework/issues

###v0.8.8 Changelog

* New name: Mobile Security Framework (MobSF)
* Added Dynamic Analysis
* VM Available for Download
* Fixed RCE
* Fixed Broken Manifest File Parsing Logic
* Sqlite DB Support
* Fixed Reporting with new PDF report
* Rescan Option
* Detect Root Detection
* Added Requiremnts.txt
* Automated Java Path Detection
* Improved Manifest and Code Analysis
* Fixed Unzipping error for Unix.
* Activity Tester Module
* Exported Activity Tester Module
* Device API Hooker with DroidMon
* SSL Certificate Pinning Bypass with JustTrustMe
* RootCloak to prevent root Detection
* Data Pusher to Dump Application Data
* pyWebproxy to decrypt SSL Traffic

###v0.8.7 Changelog

* Improved Static Analysis Rules
* Better AndroidManifest View
* Search in Files

###v0.8.6 Changelog

* Detects implicitly exported component from manifest.
* Added CFR decompiler support 
* Fixed Regex DoS on URL Regex

###v0.8.5 Changelog

* Bug Fix to support IPA MIME Type: application/x-itunes-ipa

###v0.8.4 Changelog

* Improved Android Static Code Analysis speed (2X performance)
* Static Code analysis on Dexguard protected APK.
* Fixed a Security Issue - Email Regex DoS.
* Added Logging Code.
* All Browser Support.
* MIME Type Bug fix to Support IE.
* Fixed Progress Bar.

###v0.8.3 Changelog
 
* View AndroidManifest.xml & Info.plist
* Supports iOS Binary (IPA)
* Bug Fix for Linux (Ubuntu), missing MIME Type Detection
* Check for Hardcoded Certificates
* Added Code to prevent from Directory Traversal

##Credits

* Bharadwaj Machiraju (@tunnelshade_) - For writing pyWebProxy from scratch
* Thomas Abraham - For JS Hacks on UI.
* Anto Joseph (@antojosep007) - For the help with SuperSU.
* Tim Brown (@timb_machine) - For the iOS Binary Analysis Ruleset.
* Abhinav Sejpal (@Abhinav_Sejpal) - For poking me with bugs and feature requests.
* Anant Srivastava (@anantshri) - For Activity Tester Idea

#HackingLab XsecLab Team 
* 汉化
* 优化部分性能问题
* http://www.xseclab.com/
* http://hackinglab.cn/

