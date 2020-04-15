import json
import Connectors
import Transformations
import AutoML
try:
    Adnan_DBFS = Connectors.DBFSConnector.fetch([], {}, "5e96ed40b9444966c25fe7be", spark,
                                                "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    Adnan_AutoFE = Transformations.TransformationMain.run(["5e96ed40b9444966c25fe7be"], {
                                                          "5e96ed40b9444966c25fe7be": Adnan_DBFS}, "5e96ed40b9444966c25fe7bf", spark, json.dumps({"FE": []}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(Adnan_AutoFE, [], "")

except Exception as ex:
    print(ex)
