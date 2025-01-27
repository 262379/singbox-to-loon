import json

def convert_singbox_to_loon(singbox_rules):
    loon_rules = []

    # 解析规则
    for rule in singbox_rules["rules"]:
        if "domain" in rule:
            for domain in rule["domain"]:
                loon_rules.append(f"DOMAIN,{domain},REJECT")

        if "domain_suffix" in rule:
            for suffix in rule["domain_suffix"]:
                loon_rules.append(f"DOMAIN-SUFFIX,{suffix},REJECT")

        if "domain_keyword" in rule:
            for keyword in rule["domain_keyword"]:
                loon_rules.append(f"DOMAIN-KEYWORD,{keyword},REJECT")

        if "ip_cidr" in rule:
            for cidr in rule["ip_cidr"]:
                loon_rules.append(f"IP-CIDR,{cidr},REJECT")

    return loon_rules


def main():
    # 读取 Singbox 配置文件
    with open("singbox_rules.json", "r") as f:
        singbox_rules = json.load(f)

    # 转换为 Loon 格式
    loon_rules = convert_singbox_to_loon(singbox_rules)

    # 写入到 loon_rules.conf
    with open("loon_rules.conf", "w") as f:
        f.write("[Rule]\n")
        f.write("\n".join(loon_rules))

    print("转换完成，已生成 loon_rules.conf 文件！")


if __name__ == "__main__":
    main()