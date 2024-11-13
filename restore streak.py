import requests
import json
from colorama import Fore, Style, init
init(autoreset=True)

print("""
     .-~~~-.
    /       \\
   |         |
   |  O   O  |
   |    -    |
   |   '-'   |
    \\_______/
      /   \\
     /     \\
    /       \\
   /_________\\
   
Did you lose your Snap Streak?
   :(

Contact on Telegram: @hyy_yy
""")
class ArkoseLabs:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://client-api.arkoselabs.com/fc/gt2/public_key/F2388D0C-F087-4EAB-B3B0-0358C40FE1EA"
        self.headers = {
            "Host": "client-api.arkoselabs.com",
            "Cookie": "_cfuvid=2Tcy_EqLJ0qhYnviOGCTm_1P9sZBMu9.hAx5FSqz2z4-1717104076479-0.0.1.1-604800000",
            "Content-Length": "12439",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "X-Ark-Esync-Value": "1731391200",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Ch-Ua": '"Not?A_Brand";v="99", "Chromium";v="130"',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (AbuTariq NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
            "Accept": "*/*",
            "Origin": "https://client-api.arkoselabs.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://client-api.arkoselabs.com/v2/2.11.2/enforcement.680e9fec55645f785d2cc2dbf0b3e151.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Priority": "u=1, i"
        }
        self.payload = """bda=eyJjdCI6IkExL0laUzgrZ3VYY1YySHdrdlYrQWp1bE5hUlZYdzcyWTBPTEF6RlU1RlMwSHNUa053NGpNdGxnUFduK2xicVFDZkM4R2dTVXN3SVRhdi9Xdy9oZE5LdFZxMDZTdHRsNjFRWXphUFdXVzJDQ2NndDQvdWk5cjgxNHN4YWJQbDlDUTNxSG9CMXBqN25YcmRjNkZxb0xNejJGMGtXeDlxUDFLTnMvRjFhZmFkWXl6cFo3ZFdqenpBMU5KRlh5WGhCTEhSbkdaZE8rcmticnFZcFRpWURZMTI1ZFp0ZlVaZUx5ZENPdmF3ZzdjWW5mT0twcDR6dkd5MENiTzI4bS9TMlF4T2s3bnVHako0KytjL0lhZmVVVmg4VllKSm9sWkhCUEZRRWhuVG5aektwcE5sVGxjRFc0Ky9LMlphbThPZWNMVUVhM1VTbXcveUFuMU0wV3BOKytRLzNLTUZmTkU0SmtOdjM0UzdnSC8rMW80NlRtbmlSN1k2Y3hza3dmaFNuV041aW0xNnVFbnhUQ3JhWHpmQzFVUDU0S1drcmk5djV5OEhCcVpxUk9GdXFJdDdlelpNVWtCK3NZcWxrL2JFYjZXaXROSGY1bU9JUXpVZHMrNThVMU5mZ3lMd2tNb3dscEdVZG55QTdTWUpZQXI4eXo3Yjdza3ZONHRtSUFLNWgxT3NQQkgxSnhBZWdqbEJRc21pRHhoWHF4dm1IeWR6Y3d2YzNFQXpKT05uWE5pTjN3eGEzY0JaUDZyM2FyNVJPMXZ5U3dIcC85ZnA3M1dmM1c5cExBV1hwSko0MUl1TlpISS9mQXBrM2l4YTd3NmFWdEVkNDQzL0tlSEZBdFJGMkF3cVpRVzhNckt2S05yTkNMbGdjQnlvSmNXWllTM3I5REFEQW1ZUm1nNUhKd00yYWdhc0dqN2d5K0FZTFExNmVUeEpWZC96MmNWNWJXU25QYjVaaTVLWGFLb0JiYUpoSFIrUWZ4aVJWdlB1a05GRTE1T2tpTEx1TVQ1bk8wU3RCODZhWXQyU29XMkFiNmZqWXhjVnlHRWdlZ1NWQis1ZTNJYm0xN0RLekg0TU9VcVlXUXhJalJaZ3MyQjlvNFFVaUNQc0FLMkZkaWE4ZzhqN2dJTjZCTWVlbWdMSDg1Y29IMEI3TmZTc21la3h2cHgyM0pVWGZpMGphSU9YUWlTOGFWc0Y4OURmMTMwQW5jZnNWaDNLQUQ2RnZZOHlvSWpVcEhTWHdiU3VnOXZRdXBSYVpvVXBCVWthNXFlNEJKTytuMUVQaUwxZGV0NkkzRGlWU2EwbHBYMUtoZVR3cWJhYXJLaitYUVcxdVpMc0taVTVaSUg0anU2ZWYrQ1YvNjBhNis4eHpXSmRRSnBlajVCeUdscit4SGs5VzJkb1hGMkVhcWlPL0RFL21VVVBDaHk0NVk2NlpPL3JwR1pRZ2lIYVdGVTRnM2hBOVZUQ24rdGxrbG5nNlk0K2NEQy8zV0UwSHpXQlB0NkZaV1R3Z1hLdXB3R3Jad09sTm81enZBUWw3NGpJQkR5MFNoN0hBbFMwRXRtLzVpY1hGN2ZRVUtDTEpCemtzS3Y0MDduZHZVbEI1QmpTZjlNUjRtTnNsNnZyeWd2bEJHSmlscFRCa2Nxd0dIWmltNmJManhwK0IyejVvYlpjT1prRnJEU0FDQTRXYkVhd2ovd2k0RDNJT0FuZEdJRklaSHExTS9qQm9ZSzBMbFp1MncvbUZGSE8rb3Y3a205WVBKcnBHY2ZQUHAwZlRqZm1CRktUVFdmbVBIcGllRXNzbzNZYW5ObzNrKzNiSldDVkZqckg0bnVXMy9ZcGV2dnRlcllJMjRTcitTcTlDT0JxY0diMTUwSndFM3VyaDNXWmJLNEdiL29RZ1BBcTdVQTZlTXMyeU9jTEpVb1RHQTZFVU5zQ2FTVnB3NWd0RVkrTThtalR4bldZOFA1aHRlSUdNNEJSUmNDNTY3WHIxL1JkMTVTTFVVd1YxVjBHdVdlRWpnLzZ1Rm0yMVhWVmRwdjU3Um5VcE9ESmptRStmYUMzRGhzTlNnOVZKMlRuNUptSFZwMGRSL0hoZXo1TjhLWHFMdURRa280SFA0UUFZcWphdkJIcm5zeWp2djdvMXFCWjV3UEdBa2NzaFJiUVhpc1gxOW5XNTcxVzVLblVnTDJBSjh3VE9NRVlac0tXdEtKaXR2WGptN2p5NGcxZG54M1BwSjBlNnYvM3ZxajlIZUkvd0l1U0V2cEhZNTBlY0RFaFBIdWxRL3BnbTNDaWJpek1TTjdHODV2eU04Ui9lNTltYk5OTGxVbmRYemtLbFNQQ2p1UmpRekttT1c2OVVyNnJKVzJBVVdJaTlQUVNBVmxnZ1pxUUZTYllLWDZsTWNyb0gyMWc5QUlVTC82MUh4M0xVQitmek9hV0k2eTVpSkhQRVFIVnIwTFZRcFpxcUtKalovbzVMU3F5U3RPVUZQbFBKMGlXMmJGZDhrbFNRL204QmtUc3lSYnZoeUh2R2JWUzh0Z3NiaFVUeEhWT0hIR2NVWmx2bXJ0ZVFkeUxxbnU5aGFVVzdESmg3U0lpYnhjWVpEM3FhMTJ1dU1sSHhzZjhrd1M4M2ZKd3pWOGpVQVFyVmVnTUw3Tm9nZDhhd2dVYkd5TXIyTjhtMjE1cDlsR0dLUk5QTzY5YlpFR2I0VVBIK0REcG80WHBuWDNEY0NZNVdMcThlWWZjYjYvb2FnUi9JQXFxbHNhYVF4Q0k0SjVIbjc5VlhVTks5dHRmZ1prNDR0ZXNxZDVYd1BMU0Q0Q2Z1T2ZhbnhoaU11V3VXUnIraU0zYlQ3c1dyUWRTNHh2VVNJVEx1amtwaHlDQlFaeFpaN2xvaFcrNkNpSzN0b3dkNEpLOUN4UTBpZ1N4REN4NHlLYmtrVHRFb1l4M2lUYlhvUGlLQWhRd25Ub1dIRllzU0R5cjFWakEzY3FPbWZEblZBek50WFJuWXRSS3BVV1N2SmFrdHlRbEJvWGllV2ZoTWRKRk93T0JyY0o0ejJSSlIyZ0lzUmFWZnZVd0J2TWNycEVlT3FRYXE3SVV1cFd6UFhpNnhPa2U3c3ZrZlAycU05ZmlHbWFqU0hOUDNrSHkrYlVZaUZBSExlNGVaQ28xN0lyQ3NLZkxmbTZ2MWY3NEhZQ3ZpWllQSytkODJ2UVJRMUcwUUZjdHpwNEMvZEVUOHVGY3BwanMvTnYzQm9ibGI2aW5VNTdHemZld3Q4Ujk2ZndpVWRnZzlzSEV6MGJBNTNncEhoVEJKMXBlRHIxNnNNSG95R2JEL05jdVZPNllZak0ySHBqTUVhb241a0ozenRnVzBleU5YWVU5dTZkQ1l6TkxaWFlGbisvb0RaSU5qUXNIaXZYYy9RY2VBcFd5dS9wVHRYbzFOSUxHZ3BmL2hFSG5jYU1zUm9NNjgvMXlDejRMMnR1TisrOVFLSFJQMmFHZ2Z4SlBKQ1Vhd0UyUng4OWhzK05aL1hRT2FDRlFET2MyalU0elBZRnk3dk53eDFXblBUNHZEZHFETzBsR0x3RlhHU3YxWFZmVkVKdms2VS91eVBmZG4zSUl6dEtuK2oxbit5VUs5WU9KM1QzejVFQzN2elpEUEVYMG9PQklKK25XbDRZUE53Qm1hWDBDL2tYSEhETTdKSndXZkdST3FSU2c2d3FvWmZ0R1FXZkE0K0paVmxjcnlNZzkvZUZOMzNBU05RS2RRNjNvUGhWa25PRHp2N1hIOWdEZ1hwczlSOE02ZDQ1RHF1THRKK0ZLbWNWZlVDaEJSYm9rKy9SbmV1RDNwTU1WKzFWNnp1ekIrd25BSGxrNXJydzFhT3luMXFRTWhycGdoRE1CaWdWc3A1c05DRjNDOWYrKzBydWVGU0lqSmdhUGJMQnk1c0Y0MHB3eWhYTEJqdlB4NEY1dkIyZVE2aVVlZHFsOG5YdXFEZE5MSUQwQ0Y1ZEx1RlZxWUVCUzdVTkY2c3ArRzk4S1lXQXh0aU5uZlJYcGd4MlBJYkNTdEdmbHlvc3o1c2NkSWNIVTh0UCtPMVdETjJSWXcyN05qYXhTbG1aUFErTFZSc0htU3hWenhlNnVsRkpkNlM0akIwUXhaM3BJZnRXeW00K2xaUnlwckgxbEFiVWxUSWhJRWd5Ny9lRTFzRXBMQmhaaXpUVkdWRWNuSVNjU1k4UVdZY0Q1dmVMWU1TeGo1SWdoa1JRNEM5QVNkVjhoblN2Wjl2K1htOUJUanFOZFBpUWNQNGlnUVlYNHpJQ1I4Skk5TWJUZjFORUxHb0dMM2diWDVLbnlhdVVSR1l2K0l5cWllZWJURVpxdTJLTFg4K2ZTWklnTkUwdGdxRWE4Zi92TzZ5aGZNRXNPVzZoS0oxaVlkU1R3QVV4Y0x2cUpDNXRFZkVDaTBwZGFMZHZTVGl0b3FMeTVheGZpQ0U2b2lrWlh3anhsWmkrdTBFOERBOGczZlBIU2JXQ3hiTVY1dFQ0dWJGYzVQRkUvWmlBOXpIS1FIbmFCc3FpbWgrQ2JTa0w5NkVTNytmcUJzQ0dQc3dhaUNJcUpzNXNJdFNXMmIrSUZ0cWFJY3dKN1ZaaGc4OWFNQ2w2dGtqMEszcTRLSldhZ2lxMSs1QTRyQ2Fna1JlNE9YUVlJZW4rK3pDNTVWMkVlZ1dRa21pd1hjbTk1NjBjQ0l1NG1nQVM4WHJDbTBlSmFQd1ptZlRzY3dLSVZjdGtZZ0hKZjBFSXdkWXAzam01Vnhtb2MzRk1aMk1IN3VUMzMyL3RWSE5YZ1kxZUk0OEM5MjEwMHAwSlVMVVpRQnJLM09VVkx0dDNJbU5QMkcxVldMNkNseXdOVElzM3pSK29vVEVwRzYwdUJCOS9tUnZIa0s1ajM0WkVrNFNnNmNqNVF2cmhpcmt5b2ppN2N6SThCNUp6YnhwTkVySndteVFvY051SHNPY2YvNkhvUWROMU1UWHdxcHpQYTM0ejdoQmRIQTZKYjFWVmNtMHZJZThwdndBeTBpVlo4Sm1yZjdVUUtjdEM0U2xkbzRkM0NKSkRFZGo2YnlJWGlmek9mbGVYMlgvck55MklZdUZ4S0RHb2JscVNaQ3J0b0RSV3pqZWMwUUJiM2ZlUDdMVjB0ZzZieEJEUHJOaDdrNFVYejNmQTBCRE5zT2wrNlRkNHM5b2FmZ001Ykd6OUh0c09Bakx0cUFsZnlsT2taSDBiQWFYaXl5MGxjL1ZzY3V4aWVwY0h4d2JmMHR1UzZJc3dYZUhUbG9uT3ZWUlRCdEw1dTVMSUlCZThxS1FnMjdJdHJleWNrVXlkYXNrQ3ZOTHNWaVI3RittVmF4ZWh3OTFnL1dzL0tOTW5CbjVYQTZYRHFqQWtPbHZqeXd1c05XZWlNV2hNMXYxTHpuZEhzdk40Q1dEU3NmTU9FMjREQWVKQ2l5T1NkaU56emNBanYyanlRVTNVWXpiVENVd09hRGsvamlZdnFSVTAzZVFmOHVJREM5M1FYaVBvYXJsRTVIZXF1ZnY4bENyRzRjMXdOY1lqYVg4Um9TQW9HWkFVTG1SbjRPMi9lMFFmYnZkYkJKTkY0dFpDbGdvSjBWcVplb2ZDQ2JhL0dkMkZrQTJSMTBSTXdwdnFlalMzWDU5d3IzQTY0SkZ5SDJmbC8rL0VJQ1ZUUU9Xb2duTXQ4U2RkZEFzTlU3N08zcmNEdTVQQVRJWTEwNmtlNlZLOFdSU1ErN0VCMW5LamZuZjdQOGgwMGFqQndrM3lhVzk1L0JoM1RPeDZEbDVtMFlGTVY2dzlSa2hYQmE2ei9TMWdVR0xTZHVNN3ZPWXRuYmVqaWs3NktHYnJWT21JSnhWYmF3VGp6UmVDSks0eGNucThxRm1WU0tWZU5kWHBpTFJRMC9UOWRYVDRLTG9TUTdxd1YxSFEzbDF5dlhJTWxLWG1CKzgwdVh0RjJBSmlaYldENmZLWnZhdXRWcVB5VktRa2tJaDFzazZDTzBlRUNBclFoVFVPeHVSVWx0TU1jT2RjQWp1Zk9GM280UE5SRGs5RjZ2LzZyMkJ3dHVFdTB4Q21PQXZWRnNtbGZodDZFV2ExWlNjdHhBWWVacExyZHlkR2JuTlk4VXQwR09MLzhGM0JKSFVyZjJ4OWN4MmJKNk02U3duWjdKY2xsandOM1RlcDVOTFdvL3MydVpETUwweExveFBXMXQ0M0xaRG4zajN5RlBOcEtNUFhRME8xUVVWZExQUXdWakZydGoxTVcwQ1RURFJ3ME5vclhIMFdmTUZmZ0Z1eVlXVWFMaVRmMEZUWHZDVnJ6dVhpTy9XV3FsTWkzTGxGM0NPTzl5eW8zV1VLTzR1Mmh6elBHQzNTRTlXaXp4YnJtQktFd2FWMzNweE9iaW9DREh5NjlDREtyQ0xyZk9wUXE3enZmNEJqK1g1YkZGcFkrVUQ5TXVPOUJFZWNNTEMxS2F4TXZFL09jMnA2SmxQVVhpRGtqNkpueDBDZUo1NmJHaFRjd2J6eTJ5aWpNaHRkSTloV3V4QTVQQ3dsK2hMTkFEVjZxRkhRVEc0MDloRjRzaUxlYWZKVHVpeDB3WlUzNHl6MEtCUFM5bkl0dFB0Q3FQNEJKY09QMjdRQmdqWHdyb3E3NHdKWVRLSVplVEE5SDgxWk9NYk5mNi9BMmdFdEd3VmJhRXFIUzZFak1oYkRRQUhzL3h4LzdHUUgxQmQ0VHpINTFucndhcWpKWHlDWGF4OFQ3MXoxZjAyekwvclVCTkZHUkJiWGo3blBmVEJ2amU5K3JWa3ZQSHRNZGxCUE1BbU5pbURjUnQxcFRlQ3RwcGQvTmRyVHUvWnh1cXA5SXEyT1Z4SlFyaXYwUWtUTEs4WHIrejlzYndIVW9UclRtQ1lWQXNFeGhxMlpTZ0d1VitCbi9HbWpXVWdCOUpZaUhiSkNxbm92eThNSFJ0NWxLN1d5dE5pKytJQkUyZkl5bUpFNGxHbmZaakZHMGZjdVZ5SjRXbStEVzlvYUlXZzdaUFZLNVhGTWhYU01kc2xERlBSTHE4NDRVODV2NEJHbGlWYjBlT1Q0Sk9ReU0xdzhwem5ZR3NxdWo1R1RXd25ZVFJBSm91bmFmeFdScUp2WmF6d3AxS2dXWTh0OTRtQ2dPWUhqUEViZ2x4SzhGc05ucWtGUENkZWhYblZEbUtPTlhNbWJISkwxeGJZVTdUOWw4YldVM2VITjh2T1pOQzBJUS9NU1Q2bCsxSFhKcDVYRWszaUxvMHNSVSs5aUZXQmNrZ1Q0dHpiZzlkc21QOFhMdkxhZTd3NzU0TVNtQ3VGdk15RjVrbW5ObmtvSWtpMzRQd2c0ZThXbjREYnRmSVgrY29RRU1uWi8wUHJiL3YrakJnQTArYmpOd0NQb0NiVjI2NU83Z0JFdmxCTGIvdFFvekZ2d1V1Q2d2VktoNnFSdmNlRGJSM1dYUURwVFdKYkhHUDRwenkxQS9PRzlBVW0wWGhpazBiOE1QMmZJazI5cjlQaFRyYldaVVIxeG5lNkNiTTE4L1JkRjh6Q0dWb0VreFFtbU90eitSV0t4c3BvcjhMeUR6WWZ0cFpNNUVrZy9uV242TDcwWXR5MUhpdVRFTWY3RE5kd2R3ZzV3UWw1YVRScm9MeGU2MlNpOGVqb0lJY3lCV2hwU0JiRjVXK0RQLzBaRDd1T1RudFdMNmNOTjhtNjlrRXhFQjZ0OGpadTZBUUtVMGFQeG92QUxLMUNTZ2NIS1JrOHlubURjL1pIcWxkUTdXeHpOUUwvM2tKd2x6cG5DM2NKTk5kOVpWcDQ1TG9Sc0JoVHFhYUNtUlVPSm1qdnNnSUQ1RmRSaEFubEp0a29TdldEUzBDempBaHBBRGZ1R3lJeGhOZ0hJakh2b0tacEFQdUdWTHV6QmEzaW5pdnhoQjdmMzlHVXlWazFRYTlvdFpCK0EwaVdkNFFkbmhYYk1iT0RNUHlGblFzY0F0RGVmVCs4emJtV2Z2aWdTQk5YU3gvbmdvdFVMZkhnazdVSmhQNXhZcGJNOHYyK015ZDhrQUU3dXZiYzFzWWxEM09BOHNZeHBxN2JLeUw1ZG50ZEcweVdJZ1F0cUNMZDFEUzhUQ2RVQzdyUFlGKzdiamU2VVRaYlVTRi8ySkorRGpXQ21NSDhPdlc4QWlsR2xMVXJwdzRTK1NJcDV5RG4vVnJ5MDJ6VXJvMEp6Ymd5b2dlMGRQV1lyRklaR1BMOW95U0RFZDZaeXhTTmI4TjMyVUEzVmZSWnJIN25TR1FCcTVhdVZ6TEdIRTIwM0ZKT0tHRDlyWENjQXJic0twa3V5a2FoMkhyc0Z0bWxHbWZzU2NpQkNHRzVDWEp3b20rM2NURjNVZUtjd0p2VnA3RjZWV0xkRlZxK0tBaXFtRFRRdThneGMrK2htc0RKZ21yMkU1QllxOTFZbG01dEdjSHM2a0cxNERPT2srdDhSVXJvNnNKS1RnMlNUU3dJNkt0MWcrRUt5UFRNNkw0UVErZDkxdkhBZE1uUk04SDV2WENhS2h0a2Q3eTdZY3RoQytTeUxidWt4dVJSRms3eVNjWTU5eURWM0EvYVkxbWRtV0llL1hUc1R3bStOeTdjaFJyZ1k2Q1lmSVQ4N3JEK1l2VU85b0VZUkNjQVJNY2FuZXBFbnZCQzVwK255VFNHUVBUelRTbWRNUnVKbGtLS0lCdGdIZ1BzWmJYTHJFYWlIMjNaU3dwQ1dRemkzU3RJSGlobXQwYW5BT3pFcnJnUFBIRmRmaTB3NjVsaHUvU0xxai92T3BxRzlLWUVndzZhOVBCVERNWHB0d1J5TXFNbHFXd1hNcEdQcDF6TERBazdoYTYzZkNDMW10SE9qMUQ4KzRJbWpwdmtVMHNVQmVHRjdwVlIxVkhQbnR3WXpNUEQyaDlQN0p4RTUvaXFJVHUydk5WUExrNGFpRDY5QXN6T09ac2UxNnV6N0Q2MWJIUUNxejNJaUQwYzdacUN2ZmpNMHJERExpeS9XUHhPbGlLNHFWa1dQS0RNbzlWTXJIZmZvMm9VNmY2SDAwTjBJZS9MZXJOWjZTa05BcGNMaFRyUVBDcFR0SXY2TzZyR0Rrd29kblBhQW5DcmE0YThPd01QTWUrcTk5cjhXdFBuV2lreVdCSzcyOVcvc3M4QmMwMThteDFtWGsrbUlSaDRPRDdGdzNibkJhbmROa08xaGo0UU1IeVZtZW5SSDl3cGRDeGNaTlluenlRWWN6eUhVaG9BcHV4dUlkb2cyVkZucmR0KzVjTGs5dnNKN0c3c0hHcjluamVLcUQxNmhtdDlON3RUTCtxaXJGV1JwQ29tYi82VVR0M1M3UjRVazZyNlFkK2lXS3hNSEdOL0VMWjl2UDBwcmhkakh0Q0VWc29tK1lUcGRaZXFHb2RHNXFGb0Y4bjV6c1lOL2lGU3lHUVNnYmNJTk5OSmZEcVVZSWtiMUlZMTJObHZTQ0RHSUIrSGxFUjgxMEIvV0d4QmN1RUd6OEFlZUtxSCs5ZVFrdlZsYTAxZEw3djFZaU5TSXg4ejRla1NOaXVVTGVPOEJHRk9hVGc5bVExS2tBblRQcGUyd01BeGZBV0tsNDY5RDV4V1duczh4NXlqOW1MOCt6MVk4aHRJZ2JpUGovNUFCYTZhTkdGVHNrUktmVTJnaE84Y1luOTYxVnZQeU11Q1AzVmJPbndRd1pqOXJjOGtlMEpHNzlDVmdYY2xYb2h1SkkwL0hUY0ZzOTlTaXpsOHJhcmtoY1dGL2FDbFJZRW9RYXZZS2tTWnFweVJpRGxaM1Evd0xpSDF5SWFwSWFQZWYxeHRMaDdaNFZYNEd3cm5PRjQ3RFBrd0diOVlsazNIOUVydnRqV3hnQ1kzWTNWT0JmNnpBNURFQ21vWHViYWRuY2N4WGxDd1BjeEJ6N3ZwWS95RlpuSnRPNEw4cXhIcHB4SDNxbDVqRm9OWU5RSEo5bFh1N3U1VTVSTlN5MHZVVmh2Mmw5ZUxVdXFwUlN6YllLMFBqMVBOamd5Y1lyVU55bEVvekN1SWYzTlJqUU9ueWdmbC95S2ppdWpUK3dyb01sYnVZSDg4d1RCM1ROQXp4dmM1cFNVeHprazU2Y3Q4SEN3QmRoaDZkTnpXNHNGK21oSFdDTGtIVWw1NnFDU2poRyttWWx1elQwdm9RQTU1QkdweWxOQ3FINXVvMXZ2RDZ5Ti9ESzY1M0srNHc4ZTE2RDVnQUk4WjRmb05wQk1CNHVjazZMdDQ0Y2pxa2VEUFEzZUFrNXJ3U0lGZzVENWlMTTFvaHBMelBrb29ZN0R2L1p1WmFQVTV4S1JuRHVYdnE0OU4waXVTSDZtSENCd0tqTFZyaTM2UlNRbGdxN0VNY3RST2RlOEtMaU5CVGQ1L2hXOTB6WTYxbnFvbVEzM0pUSm84QytKaHJRdjZHRmRmalBjN21zTkx0cDlBeUtDY2V4cDUyS1BOSW5INVp5ZW84WjhFeVVrUHRwTDBlRXFNL05zLzN6d0VJUXBiSzJLMnpVeG80bmkwTkJxNnYwUEFONWpwM3hoMzd2R2F2NmZBa3liZ3kzd2Y4eCs3TUZzaXJ6VmxvaTM3NGJhOTA1cnhLTUFsT1pwVkVRUXp0dTdpNW1tQTE0SGIwRi9ENUkvMjBmQ3BSQWNNVTU0TXJNU2RlODBPM3FwMi9ST0xYMFRoZ3I5Vis0NUdqRWtPc09xQ1R1ZStoTnN0N3ZmMmtlYmZrMHY0LzlhdTdkMUg5U3JSbExhSXJEOHVTT2M1bTV2MzhYZmpSWll4SS9iY3g4T2ZnUEpxbEVGQThSdE9ZTVU5eWN5aEVuUFNuWlkzRUx4UXJ2ZVhyR0RsWWx5TFZHZGh6SjlLM2hPMUI1UHBxbUoyWklDSGpKM0lZaVF3dDllQjI5SkpsMjFSbEhoTi9PRS9NL2U4dzZIWnFESjZJbVlvYjNITXpMVExlZHZRaWI4TjJ3TDRwZi8yQXJIZkdmSTk2WEtrRTk0UHErQlp5OERKanJjQml4UElaSkk3UjFXRG8vWXNIV3BnRTJWVU90Mk0zaHJZUVh6eTFOMjc4dHJtdlVCZ0lCSC84WXdCRlZrK21aMmgrYys2ZjFZa1o2Q3RDZFBxT2JpVzJ6T2xmQXNhZVRyMFVianpBenpHVFowSzZ5ZHZxTXZ4N01uS2RtcXJnZENzUUhWemxVZnAyYjlrUU82bVJHOThraTBJd2dxTDVjdXl4ei9hZG5SMEI5aE1vdHdnQ1BXMEVhUGk3WHBqVlozbDhqenhHZkRseDUybjF0VGgwd2JIV2RhRXFKRVhmS0VNYlBWWWh6ejdialVnUk01QzRiWlBHTlU1c20vTG9Hd2pyU2l4VGIzVG1VTFR3RVhyalFnck5wVU5vOWVLYkFoeEVYV3hvZ0ZWV0wrS2ppdDZlQVU0Wkd0UVJNN2c3TVBJc29QWlptakhGc3FSb1JVZzE0UGM4RFZFWWVackpwWEVCZmh1TW1keEYwQXgvSUlCbXErdW1WdkZPS0g1ZTQwOU5mSVlzdSszKy82UE5OMmNkMHNQamUzZktHK05TZDZ2VEc2WlJlZmJ5VDAreDNUdnM2TE5yakZYdWJmMmdlUFY4dWtzSTJQQndjWFNHR3YzR3hFVW1TTTRlRG9nVFZJbHdDWFYvQUlpeVArbEV5WFU1TlpRMlB3S1ZkZ2c2UWxMNzhhdmx6bFBuSDZYWFFrRmlxcDRSd1BJZEdaNlZOczFTZDJ1SU44emtaWWNzMitYYlZzMjdiU05Vb0QvWXFNWEQ1UlBpa0Z6T1RZZ0VWNHpRaXF2ZUZOc1g2TUpteXJzSllYaGp4ZXg2a0MzTlQwS3NkNFk0cnp2TWtSWWdQbEFUTnZ4RTFrM1dqQS9nV2VrcGFiUEV4Si9jbWZ5Vi9aMUZLZFJGWitvZjRwdkRiMjhaeDJkdXhPVlRJaVN4OWxWZTF6L2R4c3ZwVVVSQWNjU3NhRUtJR1dwcU1sT3FJbURPZz09IiwicyI6ImQ3ZTU4NjcwN2UzMWIxZjgiLCJpdiI6ImVhNjc5OGEyZDA3ZTI1ZjIzOTBlYTI3ZWE0ZTUwNWRhIn0%3D&public_key=F2388D0C-F087-4EAB-B3B0-0358C40FE1EA&site=https%3A%2F%2Fiframe.arkoselabs.com&userbrowser=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F130.0.6723.70%20Safari%2F537.36&capi_version=2.11.2&capi_mode=lightbox&style_theme=default&rnd=0.43533380885014905&data[blob]=undefined"""
    def fetch_token(self):
        print(Fore.CYAN + Style.BRIGHT + "Fetching Arkose Labs token...")
        try:
            response = self.session.post(self.url, data=self.payload, headers=self.headers)
            response.raise_for_status()
            data = json.loads(response.text)
            token = data.get("token")
            if token:
                print(Fore.GREEN + "Token fetched successfully!")
                return token
            else:
                print(Fore.RED + "Error: Token not found in the response.")
        except requests.RequestException as e:
            print(Fore.RED + f"An error occurred: {e}")
        return None
class SnapAPI:
    def __init__(self, arkose_token):
        self.url = "https://wassupsnap.appspot.com/en-US/api/v2/zendesk/send"
        self.headers = {
            "Host": "wassupsnap.appspot.com",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryUtRXubGndIQW5VW6",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
        }
        self.arkose_token = arkose_token

    def send_request(self, username, email, friend):
        data = f'''------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="key"

snapstreaks-restore
------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="answers"


------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="arkose-token"

{self.arkose_token}
------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="field-24281229"

{username}
------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="field-24335325"

{email}
------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="field-24369716"

966512345678
------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="field-24369736"

{friend}
------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="field-22808619"

This field intentionally left blank
------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="tags"


------WebKitFormBoundaryUtRXubGndIQW5VW6
Content-Disposition: form-data; name="is_treatment"

True
------WebKitFormBoundaryUtRXubGndIQW5VW6--
'''
        print(Fore.CYAN + Style.BRIGHT + "Sending request to Snap API...")
        try:
            response = requests.post(self.url, headers=self.headers, data=data)
            response.raise_for_status()
            print(Fore.GREEN + "Request sent successfully!")
            input(Fore.YELLOW + "The streak has been restored. If it hasn't been successfully restored, please submit again and ensure the provided information is accurate ... :) ")
        except requests.RequestException as e:
            print(Fore.RED + f"An error occurred: {e}")
def main():
    arkose = ArkoseLabs()
    token = arkose.fetch_token()
    
    if token:
        username = input(Fore.CYAN + "Enter Username: ")
        email = input(Fore.CYAN + "Enter Email: ")
        friend = input(Fore.CYAN + "Enter Friend Username: ")
        
        snap_api = SnapAPI(token)
        snap_api.send_request(username, email, friend)
    else:
        print(Fore.RED + "Unable to retrieve token. Exiting...")


if __name__ == "__main__":
    main()
