# -*- coding: utf-8 -*-
# @Time    : 2/21/2024 7:54 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : FeederCondition.py
# @Software: PyCharm
import py_dss_interface


class FeederCondition:

    @classmethod
    def set_capacitor_status(cls, dss: py_dss_interface.DSS, capacitor: bool):
        if not capacitor:
            v = "no"
            dss.text(f"batchedit capacitor..* enabled={v}")

    @classmethod
    def set_load_level_condition(cls, dss: py_dss_interface.DSS, load_mult: float):
        dss.text(f"set loadmult={load_mult}")
        dss.text("solve")

    @classmethod
    def consider_existing_gen(cls, dss: py_dss_interface.DSS, value: bool = False):
        if value:
            v = "yes"
        else:
            v = "no"
        dss.text(f"batchedit generator..* enabled={v}")
        dss.solution.solve()

    @classmethod
    def set_existing_gen_mult(cls, dss: py_dss_interface.DSS, value: float = 1):

        dss.generators.first()
        for _ in range(dss.generators.count):
            dss.generators.kw = dss.generators.kw * value
            dss.generators.kva = dss.generators.kva * value
            dss.generators.kvar = dss.generators.kvar * value
            dss.generators.next()

        dss.solution.solve()

    @classmethod
    def set_load_model(cls, dss: py_dss_interface.DSS):
        dss.text(f"batchedit load..* model=1")
        dss.text("batchedit load..* vmaxpu=1.15")
        dss.text("batchedit load..* vminpu=0.0001")
        dss.text("batchedit load..* vlowpu=0.00001")

    @classmethod
    def set_generator_model(cls, dss: py_dss_interface.DSS):
        dss.text("batchedit generator..* vmaxpu=1.15")
        dss.text("batchedit generator..* vminpu=0.0001")

    @classmethod
    def push_regulators(cls, dss: py_dss_interface.DSS, push_reg: int):  # TODO when it is for new load, option 1 should provide the button of the band

        dss.text("Batchedit generator..* enabled=No")
        if push_reg == 0:
            dss.text("set controlmode=off")
        elif push_reg == 1 or push_reg == 2:
            tr_tap = dict()

            dss.regcontrols.first()
            for _ in range(dss.regcontrols.count):
                vreg = dss.regcontrols.forward_vreg
                band = dss.regcontrols.forward_band
                base_v = dss.regcontrols.pt_ratio  # TODO improve it

                if push_reg == 1:
                    v = (vreg + 1 / 2 * band) / 120 # TODO checking if it is load or gen.
                    # v = (vreg - 1 / 2 * band) / 120 # TODO checking if it is load or gen.
                elif push_reg == 2:
                    v = vreg / 120
                tr_tap[dss.regcontrols.transformer] = v
                dss.regcontrols.forward_band = 0.0001
                dss.regcontrols.forward_vreg = v * 120

                dss.regcontrols.next()

            if tr_tap:
                for tr, tap in tr_tap.items():
                    dss.transformers.name = tr
                    dss.transformers.num_taps = 1000

                dss.text("set maxcontroli=1000000")
                dss.solution.solve()

            if tr_tap:
                for tr, tap in tr_tap.items():
                    dss.transformers.name = tr
                    dss.transformers.wdg = 2
                    dss.transformers.tap = dss.transformers.tap

                dss.text("set controlmode=off")
                # dss.text("batchedit capacitor..* enabled=no")

                dss.solution.solve()

    @classmethod
    def existing_generation(cls, dss: py_dss_interface.DSS, add: bool = False, mult_existing_gen: float = 1):
        bus_gen = list()
        if add:

            dss.generators.first()

            for _ in range(dss.generators.count):
                dss.circuit.set_active_element(f"generator.{dss.generators.name}")
                name = dss.generators.name
                bus = dss.cktelement.bus_names[0].split(".")[0]
                kv = dss.generators.kv
                kw = dss.generators.kw * mult_existing_gen

                dss.text(f"new load.{name} kv={kv} bus1={bus} kw={-kw} pf=1 model=5 status=fixed")  # TODO test with load

                bus_gen.append(dss.cktelement.bus_names[0].split(".")[0])

                dss.generators.next()

            dss.text("Batchedit generator..* enabled=No")
            # dss.text("Batchedit generator..* enabled=Yes kw=500")
            dss.solution.solve()

        else:
            dss.text("Batchedit generator..* enabled=No")
            # dss.text("Batchedit generator..* enabled=Yes kw=500")
            dss.solution.solve()
