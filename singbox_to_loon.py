import json

def convert_singbox_to_loon(singbox_rules):
    loon_rules = []

    # 解析规则
    for rule in singbox_rules["rules"]:
        if "domain" in rule:
            for domain in rule["domain"]:
                loon_rules.append(f"DOMAIN,{domain}")

        if "domain_suffix" in rule:
            for suffix in rule["domain_suffix"]:
                loon_rules.append(f"DOMAIN-SUFFIX,{suffix}")

        if "domain_keyword" in rule:
            for keyword in rule["domain_keyword"]:
                loon_rules.append(f"DOMAIN-KEYWORD,{keyword}")

        if "ip_cidr" in rule:
            for cidr in rule["ip_cidr"]:
                loon_rules.append(f"IP-CIDR,{cidr}")

    return loon_rules


def main():
    # 打开 JSON 文件并忽略注释
    with open("singbox_rules.json", "r") as f:
        json_data = f.read()

    # 移除 JSON 风格的注释（`//` 开头的行）
    lines = json_data.splitlines()
    cleaned_lines = [
        line for line in lines if not line.strip().startswith("//")
    ]
    cleaned_json = "\n".join(cleaned_lines)

    # 加载 JSON 数据
    singbox_rules = json.loads(cleaned_json)

    # 转换为 Loon 格式
    loon_rules = convert_singbox_to_loon(singbox_rules)

    # 写入到 loon_rules.conf
    with open("loon_rules.conf", "w") as f:
        f.write("# Loon Rules (converted from Singbox)\n")
        f.write("[Rule]\n")
        f.write("\n".join(loon_rules))

    print("转换完成，已生成 loon_rules.conf 文件！")


if __name__ == "__main__":
    main()
