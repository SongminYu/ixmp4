# type: ignore
"""Normalize Indexset.data storage

Revision ID: 914991d09f59
Revises: 0d73f7467dab
Create Date: 2024-10-29 15:37:51.485552

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import sqlite

# Revision identifiers, used by Alembic.
revision = "914991d09f59"
down_revision = "0d73f7467dab"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "optimization_indexsetdata",
        sa.Column("indexset__id", sa.Integer(), nullable=False),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=False, on_null=True, start=1, increment=1),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["indexset__id"],
            ["optimization_indexset.id"],
            name=op.f(
                "fk_optimization_indexsetdata_indexset__id_optimization_indexset"
            ),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_optimization_indexsetdata")),
        sa.UniqueConstraint(
            "indexset__id",
            "value",
            name=op.f("uq_optimization_indexsetdata_indexset__id_value"),
        ),
    )
    with op.batch_alter_table("optimization_indexsetdata", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_optimization_indexsetdata_indexset__id"),
            ["indexset__id"],
            unique=False,
        )

    with op.batch_alter_table("optimization_indexset", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "_data_type",
                sa.Enum("float", "int", "str", native_enum=False),
                nullable=True,
            )
        )
        batch_op.drop_column("elements")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("optimization_indexset", schema=None) as batch_op:
        batch_op.add_column(sa.Column("elements", sqlite.JSON(), nullable=False))
        batch_op.drop_column("_data_type")

    with op.batch_alter_table("optimization_indexsetdata", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_optimization_indexsetdata_indexset__id"))

    op.drop_table("optimization_indexsetdata")
    # ### end Alembic commands ###