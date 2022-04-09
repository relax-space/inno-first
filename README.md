# inno-first

## 如何开始

1. 安装 https://jrsoftware.org/isdl.php
2. 安装指引一步一步来就好


## 注意事项
1. 文件非常好加, 直接多选即可
1. 子文件夹: 要选择最后的叶子节点, 如果实在太多,可以先只选顶级文件夹,然后再去改脚本,
    如果还是觉得麻烦,这里提供了一份python脚本,自动生成
``` bash
# 下面是添加 文件 和 文件夹的区别
Source: "C:\Users\Administrator\Desktop\okjx\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Administrator\Desktop\okjx\aiohttp\*"; DestDir: "{app}\aiohttp"; Flags: ignoreversion recursesubdirs createallsubdirs
```
2. 签名: 不签名就有可能会被杀毒软件提示, 但是inno的签名功能完全没法用, 最终放弃,选择[手动签名](https://github.com/relax-space/sign-first) [手动签名gitee仓库](https://gitee.com/relax-space/sign-first)

## 脚本的使用

1. 配置: 直接把父级路径放进去即可
``` python
if __name__ == '__main__':
    parent_dir = r'C:\Users\Administrator\Desktop\okjx'
    main_inno(parent_dir)
```

2. 测试效果
```
终端执行 tree .

└─a1
    ├─b1
    │  ├─c1
    │  └─c2
    ├─b2
    │  ├─c3
    │  │  └─d1
    │  └─c4
    └─b3

python main.py
['a1\\b1\\c1', 'a1\\b1\\c2', 'a1\\b2\\c3\\d1', 'a1\\b2\\c4', 'a1\\b3']
```

```
├─aiohttp
├─certifi
├─Crypto
│  ├─Cipher
│  ├─Hash
│  ├─Math
│  ├─Protocol
│  ├─PublicKey
│  └─Util
├─frozenlist
├─multidict
├─relax
└─yarl

Source: "C:\Users\Administrator\Desktop\okjx\aiohttp\*"; DestDir: "{app}\aiohttp"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\certifi\*"; DestDir: "{app}\certifi"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\Crypto\Cipher\*"; DestDir: "{app}\Crypto\Cipher"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\Crypto\Hash\*"; DestDir: "{app}\Crypto\Hash"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\Crypto\Math\*"; DestDir: "{app}\Crypto\Math"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\Crypto\Protocol\*"; DestDir: "{app}\Crypto\Protocol"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\Crypto\PublicKey\*"; DestDir: "{app}\Crypto\PublicKey"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\Crypto\Util\*"; DestDir: "{app}\Crypto\Util"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\frozenlist\*"; DestDir: "{app}\frozenlist"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\multidict\*"; DestDir: "{app}\multidict"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\relax\*"; DestDir: "{app}\relax"; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Administrator\Desktop\okjx\yarl\*"; DestDir: "{app}\yarl"; Flags: ignoreversion recursesubdirs
PS D:\1.source\pythonpath\inno-first> cd C:\Users\Administrator\Desktop\okjx

```

