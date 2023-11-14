// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class HaQueryDistinctClause extends TeaModel {
    /**
     * <p>要打散的字段</p>
     */
    @NameInMap("dist_key")
    @Validation(required = true)
    public String distKey;

    /**
     * <p>一轮抽取的文档数</p>
     */
    @NameInMap("dist_count")
    public String distCount;

    /**
     * <p>抽取的轮数</p>
     */
    @NameInMap("dist_times")
    public String distTimes;

    /**
     * <p>是否保留抽取之后剩余的文档。如果为false，为不保留，则搜索结果的total（总匹配结果数）会不准确。</p>
     */
    @NameInMap("reserved")
    public String reserved;

    /**
     * <p>过滤条件，被过滤的doc不参与distinct，只在后面的排序中，这些被过滤的doc将和被distinct出来的第一组doc一起参与排序。默认是全部参与distinct。</p>
     */
    @NameInMap("dist_filter")
    public String distFilter;

    /**
     * <p>当reserved为false时，设置update_total_hit为true，则最终total_hit会减去被distinct丢弃的数目（不一定准确），为false则不减。</p>
     */
    @NameInMap("update_total_hit")
    public String updateTotalHit;

    /**
     * <p>指定档位划分阈值，所有的文档将根据档位划分阈值划分成若干档，每个档位中各自根据distinct参数做distinct，可以不指定该参数，默认是所有文档都在同一档。档位的划分按照文档排序时第一维的排序依据的分数进行划分，两个档位阈值之间用 “|” 分开，档位的个数没有限制。例如：1、grade:3.0 ：表示根据第一维排序依据的分数分成两档，(< 3.0)的是第一档，(>= 3.0) 的是第二档；2、grade:3.0|5.0 ：表示分成三档，(< 3.0)是第一档，(>= 3.0，< 5.0)是第二档，(>= 5.0)是第三档。档位的先后顺序和第一维排序依据的顺序一致，即如果第一维排序依据是降序，则档位也是降序，反之亦然。</p>
     */
    @NameInMap("grade")
    public String grade;

    public static HaQueryDistinctClause build(java.util.Map<String, ?> map) throws Exception {
        HaQueryDistinctClause self = new HaQueryDistinctClause();
        return TeaModel.build(map, self);
    }

    public HaQueryDistinctClause setDistKey(String distKey) {
        this.distKey = distKey;
        return this;
    }
    public String getDistKey() {
        return this.distKey;
    }

    public HaQueryDistinctClause setDistCount(String distCount) {
        this.distCount = distCount;
        return this;
    }
    public String getDistCount() {
        return this.distCount;
    }

    public HaQueryDistinctClause setDistTimes(String distTimes) {
        this.distTimes = distTimes;
        return this;
    }
    public String getDistTimes() {
        return this.distTimes;
    }

    public HaQueryDistinctClause setReserved(String reserved) {
        this.reserved = reserved;
        return this;
    }
    public String getReserved() {
        return this.reserved;
    }

    public HaQueryDistinctClause setDistFilter(String distFilter) {
        this.distFilter = distFilter;
        return this;
    }
    public String getDistFilter() {
        return this.distFilter;
    }

    public HaQueryDistinctClause setUpdateTotalHit(String updateTotalHit) {
        this.updateTotalHit = updateTotalHit;
        return this;
    }
    public String getUpdateTotalHit() {
        return this.updateTotalHit;
    }

    public HaQueryDistinctClause setGrade(String grade) {
        this.grade = grade;
        return this;
    }
    public String getGrade() {
        return this.grade;
    }

}
