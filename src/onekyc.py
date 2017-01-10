from bitcoin import *

master_addr = "1JM58KNU3K8YFV4MVXSF9owP3iYVknLWJu"

def create_metadata_hash(doc, uid):
    return sha256(sha256(doc) + uid)

def post_transaction(doc, uid):
    bank_priv = get_bank_priv()

    inputs = history(pubtoaddr(privtopub(bank_priv)))
    outputs = history(master_addr)

    print "in: ", inputs
    print "out: ", outputs

    outputs.append({"value": 70191, "address": master_addr})

    #tx = mksend(inputs, outputs, master_addr, 1403)
    tx = mktx(inputs, outputs)

    #print tx
    #msg = create_metadata_hash(doc, uid)
    #tx_msg = mk_opreturn(msg, tx)

    signed_tx = sign(tx, 1, bank_priv)
    print signed_tx

    pushtx(tx)
    return "https://blockchain.info/tx/" + signed_tx

def get_bank_priv():
    with open ("master.priv", "r") as f:
        priv = f.readlines()[0].rstrip()
        return priv


def main():
    doc = "sample hello"
    uid = "sample uid"

    url = post_transaction(doc, uid)
    print url

if __name__ == '__main__':
    main()
