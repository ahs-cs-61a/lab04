mainTestCommand='python3 -m pytest -s tests/test.py -k test_'
alias install_pytest='python3 -m pip install pytest'
alias import_packs='python3 -m pip install -e .'
alias wwpd='python3 main.py'
alias test_all='python3 -m pytest -s tests/test.py'
run_test () {
    eval '$mainTestCommand$1'
}
